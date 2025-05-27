from app.core.classes.abstract_generator import BlogContentGenerator

class TravelGenerator(BlogContentGenerator):
    def _build_prompt(self) -> str:
        return f"""
            Create a detailed post with at least 800 words (not counting the title) about {self.segment} {self.topic} using STRICT MARKDOWN FORMATTING and following this structure:

            ```markdown
            # [Creative Title Here] 🌍✈️

            ## Introduction
            [Engaging introduction in 2–3 sentences]

            ## [Section Name 1]
            - Practical tip 1
            - Practical tip 2

            ## [Section Name 2]
            - Practical tip 3
            - Practical tip 4

            ## [Section Name 3]
            - Practical tip 5
            - Practical tip 6

            ### Conclusion
            [Inspirational closing paragraph]
            [CTA inviting readers to share their own experiences]
            ```

            Requirements:
            1. The title must be an H1 (#)
            2. All main sections must be H2 (##)
            3. Include exactly three sections (excluding the introduction and conclusion)
            4. Include a minimum of six practical tips in total (two per section)
            5. The CTA must be an open-ended question
            6. Use an inspirational tone with accessible language
            7. Keep the focus on {self.segment} throughout
            8. Feel free to use travel-related emojis in the title
            9. The post must be at least 800 words long (excluding the title)
        """
