from app.core.classes.abstract_model import LLMModel
from app.generators.travel_generator import TravelGenerator
from app.generators.tech_generator import TechGenerator

class GeneratorFactory:
    @staticmethod
    def create_generator(segment: str, llm_model: LLMModel):
        if segment == "viagens":
            return TravelGenerator(segment, llm_model)
        elif segment == "tecnologia":
            return TechGenerator(segment, llm_model)
        else:
            raise ValueError("Segmento inválido")
