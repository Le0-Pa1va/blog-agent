from app.core.classes.abstract_generator import BlogContentGenerator


class TechGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
            Generate a technical post with at least 800 words (excluding the title) about {self.segment} {self.topic} using STRICT MARKDOWN FORMATTING with the following structure:

            ```markdown
            # [Impactful Title]

            ## Introduction
            [Brief context about the technology in 2–3 sentences]

            ## Advantages
            ### 1. [Main Advantage]
            [Technical explanation in 2–3 paragraphs]

            ### 2. [Second Advantage]
            [Technical explanation in 2–3 paragraphs]
            ```python
            # Relevant code example (if applicable)
            ```

            ## Challenges
            ### [Main Challenge]
            [Technical analysis in 1–2 paragraphs]

            ## Conclusion
            [Concise summary]
            [CTA asking about experiences with the technology]
            ```

            Mandatory requirements:
            1. Title must be an H1 (`#`)
            2. "Advantages" and "Challenges" sections must use H2 (`##`)
            3. Subtopics must use H3 (`###`)
            4. Include **at least one code block** (if applicable to the technology)
            5. CTA must be a **technical open-ended question**
            6. Professional but accessible tone
            7. Minimum of **800 words**
        """
