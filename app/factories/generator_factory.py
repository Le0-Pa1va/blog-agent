from app.core.classes.abstract_model import LLMModel
from app.generators.travel_generator import TravelGenerator
from app.generators.tech_generator import TechGenerator

class GeneratorFactory:
    @staticmethod
    def create_generator(segment: str, llm_model: LLMModel, topic: str):
        if segment == "travel":
            return TravelGenerator(segment, llm_model, topic)
        elif segment == "tech":
            return TechGenerator(segment, llm_model, topic)
        else:
            raise ValueError("Segmento inválido")
