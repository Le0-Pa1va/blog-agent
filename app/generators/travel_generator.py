from app.core.classes.abstract_generator import BlogContentGenerator

class TravelGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
        Gere um post sobre {self.segment} com:
        - Título criativo
        - 3 seções com dicas práticas
        - Tom inspirador
        - CTA convidando para compartilhar experiências
        """

    def _format_content(self, raw_text: str) -> str:
        return f"✈️ {raw_text}\n\n📍 Partiu explorar? Comente abaixo! 📍"
