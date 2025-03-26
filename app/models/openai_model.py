from openai import OpenAI
from dotenv import load_dotenv
import os
from app.core.classes.abstract_model import LLMModel


load_dotenv()

class OpenAIModel(LLMModel):
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_content(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL_NAME"),
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
