from abc import ABC, abstractmethod
from typing import Optional

from app.core.classes.abstract_model import LLMModel

class BlogContentGenerator(ABC):
    def __init__(self, segment: str, llm_model: LLMModel, topic: str):
        self.segment = segment
        self.llm_model = llm_model
        self.topic = topic

    def generate_post(self) -> str:
        """Concrete method that defines the standard generation workflow"""
        prompt = self._build_prompt()
        raw_content = self.llm_model.generate_content(prompt)

        return self._format_content(raw_content)


    def _format_content(self, raw_text: str) -> str:
        """
        Processes markdown content and extracts structured components.

        Extracts:
        - The title (first H1 heading found)
        - Keeps the full markdown content

        Args:
            raw_text (str): Raw text in markdown format

        Returns:
            dict: Dictionary with the processed components containing:
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
        """Abstract method: each subclass defines its own prompt"""
        pass
