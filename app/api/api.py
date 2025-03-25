from fastapi import APIRouter, Depends

from app.api.schemas import AgentRequest
from app.factories.generator_factory import GeneratorFactory
from app.factories.model_factory import ModelFactory

agent_router = APIRouter()

@agent_router.get("/")
async def generate_post(request: AgentRequest = Depends()):
    try:
        llm = ModelFactory.create_model(request.model.value)
        generator = GeneratorFactory.create_generator(request.segment.value, llm)
        post = generator.generate_post()

        return {
            "model": request.model.value,
            "segment": request.segment.value,
            "post": post
        }

    except ValueError as e:
        return {"Erro: {e}"}

