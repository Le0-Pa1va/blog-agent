import google.generativeai as genai
from dotenv import load_dotenv
import os
from app.core.classes.abstract_model import LLMModel


load_dotenv()

class GeminiModel(LLMModel):
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model_name=os.getenv("GEMINI_MODEL_NAME"))

    def generate_content(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
