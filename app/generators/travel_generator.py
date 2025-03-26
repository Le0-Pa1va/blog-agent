from app.core.classes.abstract_generator import BlogContentGenerator

class TravelGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
            Gere um post detalhado de, no mínimo, 800 palavras sobre {self.segment} {self.topic} usando FORMATAÇÃO MARKDOWN ESTRITA com a seguinte estrutura:

            ```markdown
            # [Título Criativo Aqui]

            ## Introdução
            [Introdução atraente de 2-3 frases]

            ## [Nome da Seção 1]
            - Dica prática 1
            - Dica prática 2

            ## [Nome da Seção 2]
            - Dica prática 3
            - Dica prática 4

            ## [Nome da Seção 3]
            - Dica prática 5
            - Dica prática 6

            ### Conclusão
            [Encerramento inspirador]
            [CTA convidando os leitores a compartilhar experiências]
            ```

            Requisitos:
            1. O título deve ser H1 (#)
            2. As seções devem ser H2 (##)
            3. Incluir exatamente 3 seções
            4. Mínimo de 6 dicas práticas no total
            5. O CTA deve fazer uma pergunta aberta
            6. Use tom inspirador e linguagem acessível
            7. Mantenha o foco em {self.segment}
            8. Pode usar emojis relacionados a viagem no título
            9. Mínimo de 800 palavras
        """
