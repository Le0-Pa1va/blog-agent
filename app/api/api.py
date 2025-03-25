from fastapi import APIRouter

from app.factories.generator_factory import GeneratorFactory
from app.factories.model_factory import ModelFactory

agent_router = APIRouter()

@agent_router.get("/")
async def root():
    modelo = "gemini"
    segmento = "tecnologia"

    try:
        llm = ModelFactory.create_model(modelo)
        gerador = GeneratorFactory.create_generator(segmento, llm)

        post = gerador.generate_post()

        return {"Post": post}

    except ValueError as e:
        return {"Erro: {e}"}

