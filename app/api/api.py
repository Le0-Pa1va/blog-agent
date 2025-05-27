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
        Endpoint for automated blog post generation via LLM.

        Description:
            Uses large language models (LLM) to create structured content
            based on the specified segment.

        Parameters:
            - **model** (ModelName):
                - Type: Enum string
                - Large language model (LLM) to use
                - Options: `gpt` (OpenAI) or `gemini` (Google)
                - Default: `gemini`

            - **segment** (SegmentName):
                - Type: Enum string
                - Content niche for the post
                - Options: `technology` or `travel`
                - Default: `technology`

        Returns:
            {
                'model': str,
                'segment': str,
                'post': str
            }

        Error Codes:
            400: Invalid parameters
            500: Content generation error
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
