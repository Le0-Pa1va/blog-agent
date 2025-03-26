from app.core.classes.abstract_generator import BlogContentGenerator


class TechGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
            Gere um post técnico de, no mínimo, 800 palavras (sem contar o título) sobre {self.segment} {self.topic} usando FORMATAÇÃO MARKDOWN ESTRITA com a seguinte estrutura:

            ```markdown
            # [Título Impactante]

            ## Introdução
            [Contexto breve sobre a tecnologia em 2-3 frases]

            ## Vantagens
            ### 1. [Vantagem Principal]
            [Explicação técnica com 2-3 parágrafos]

            ### 2. [Segunda Vantagem]
            [Explicação técnica com 2-3 parágrafos]
            ```python
            # Exemplo de código relevante (se aplicável)
            ```

            ## Desafios
            ### [Principais Desafio]
            [Análise técnica com 1-2 parágrafos]

            ## Conclusão
            [Resumo conciso]
            [CTA perguntando sobre experiências com a tecnologia]
            ```

            Requisitos obrigatórios:
            1. Título como H1 (#)
            2. Seções de Vantagens/Desafios como H2 (##)
            3. Subtópicos como H3 (###)
            4. Incluir pelo menos 1 bloco de código (se aplicável à tecnologia)
            5. CTA deve ser uma pergunta aberta técnica
            6. Tom profissional mas acessível
            7. Mínimo de 800 palavras
        """
