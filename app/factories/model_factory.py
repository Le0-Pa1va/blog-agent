from app.core.classes.abstract_model import LLMModel
from app.models.openai_model import OpenAIModel
from app.models.gemini_model import GeminiModel


class ModelFactory:
    @staticmethod
    def create_model(model_name: str) -> LLMModel:
        if model_name == "gpt":
            return OpenAIModel()
        elif model_name == "gemini":
            return GeminiModel()
        else:
            raise ValueError("Modelo não suportado")
