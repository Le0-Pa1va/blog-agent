from fastapi import APIRouter, Depends

from app.api.schemas import AgentRequest
from app.factories.generator_factory import GeneratorFactory
from app.factories.model_factory import ModelFactory

agent_router = APIRouter()

@agent_router.get("/")
async def generate_post(request: AgentRequest = Depends())-> dict:
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

        return {
            "model": request.model.value,
            "segment": request.segment.value,
            "post": post
        }

    except ValueError as e:
        return {"Erro: {e}"}

