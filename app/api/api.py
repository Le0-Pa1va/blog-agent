from fastapi import APIRouter, Depends, HTTPException

from app.api.schemas import AgentRequest
from app.dependencies import get_db
from app.factories.generator_factory import GeneratorFactory
from app.factories.model_factory import ModelFactory

agent_router = APIRouter()

@agent_router.get("/generate")
async def generate_post(
    request: AgentRequest = Depends(),
    db=Depends(get_db)
)-> dict:
    """
        Endpoint para geração automatizada de posts de blog via LLM.

        Descrição:
            Utiliza modelos de language model (LLM) para criar conteúdo
            estruturado baseado no segmento especificado.

        Parâmetros:
            - **model** (ModelName):
                - Tipo: Enum string
                - Modelo de large language model (LLM)
                - Options: `gpt` (OpenAI) ou `gemini` (Google)
                - Default: `gemini`

            - **segment** (SegmentName):
                - Tipo: Enum string
                - Nicho de conteúdo para o post
                - Options: `technology` (tecnologia) ou `travel` (viagens)
                - Default: `technology`

        Retorno:
            {
                'model': str,
                'segment': str,
                'post': str
            }

        Error Codes:
            400: Parâmetros inválidos
            500: Erro na geração do conteúdo
    """
    try:
        llm = ModelFactory.create_model(request.model.value)
        generator = GeneratorFactory.create_generator(request.segment.value, llm, request.topic)
        post = generator.generate_post()
        post_data = {
            "model": request.model.value,
            "segment": request.segment.value,
            "title": post.get("title", ""),
            "content": post.get("content", ""),
            "topic": request.topic
        }

        await db["posts"].insert_one(post_data)

        return {
            "model": request.model.value,
            "segment": request.segment.value,
            "post": post
        }

    except ValueError as e:
        return {"Erro: {e}"}


@agent_router.get("/list")
async def generate_post(
    db=Depends(get_db)
)-> dict:
    try:
        posts_cursor = db["posts"].find()
        posts = await posts_cursor.to_list()
        response = {post.get("title"): post.get("content") for post in posts}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
