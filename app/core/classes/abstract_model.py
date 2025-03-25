from abc import ABC, abstractmethod

class LLMModel(ABC):
    @abstractmethod
    def generate_content(self, prompt: str) -> str:
        """Método abstrato para gerar texto"""
        pass
