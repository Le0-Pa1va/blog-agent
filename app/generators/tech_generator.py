from app.core.classes.abstract_generator import BlogContentGenerator


class TechGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
        Gere um post técnico sobre {self.segment} com:
        - Título impactante
        - 2 vantagens e 1 desafio
        - Exemplos de código (se aplicável)
        - CTA perguntando sobre uso da tecnologia
        """

    def _format_content(self, raw_text: str) -> str:
        return f"```python\n# {self.segment.upper()}\n{raw_text}\n```"