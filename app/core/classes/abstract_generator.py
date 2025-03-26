from abc import ABC, abstractmethod
from typing import Optional

from app.core.classes.abstract_model import LLMModel

class BlogContentGenerator(ABC):
    def __init__(self, segment: str, llm_model: LLMModel, topic: str):
        self.segment = segment
        self.llm_model = llm_model
        self.topic = topic

    def generate_post(self) -> str:
        """Método concreto que define o fluxo padrão de geração"""
        prompt = self._build_prompt()
        raw_content = self.llm_model.generate_content(prompt)

        return self._format_content(raw_content)


    def _format_content(self, raw_text: str) -> str:
        """
        Processa conteúdo em markdown e extrai componentes estruturados.

        Extrai:
        - O título (primeiro heading H1 encontrado)
        - Mantém o conteúdo markdown completo

        Args:
            raw_text (str): Texto bruto em formato markdown

        Returns:
            dict: Dicionário com os componentes processados contendo:
                {
                    'title': str,
                    'content': str,
                }
        """
        title = ""
        for line in raw_text.split('\n'):
            if line.startswith('# ') and not title:
                title = line[2:].strip()

        return {
            'title': title,
            'content': raw_text,
        }


    @abstractmethod
    def _build_prompt(self) -> str:
        """Método abstrato: cada subclasse define seu prompt"""
        pass
