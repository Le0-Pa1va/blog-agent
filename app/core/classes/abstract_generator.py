from abc import ABC, abstractmethod
from typing import Optional

class BlogContentGenerator(ABC):
    def __init__(self, segment: str, llm_model):
        self.segment = segment
        self.llm_model = llm_model

    def generate_post(self) -> str:
        """Método concreto que define o fluxo padrão de geração"""
        # 1. Construir o prompt (delegado para as subclasses)
        prompt = self._build_prompt()

        # 2. Gerar conteúdo bruto via LLM
        raw_content = self.llm_model.generate_content(prompt)

        # 3. Formatar (delegado para as subclasses)
        return self._format_content(raw_content)

    @abstractmethod
    def _build_prompt(self) -> str:
        """Método abstrato: cada subclasse define seu prompt"""
        pass

    @abstractmethod
    def _format_content(self, raw_text: str) -> str:
        """Método abstrato: formatação específica por segmento"""
        pass