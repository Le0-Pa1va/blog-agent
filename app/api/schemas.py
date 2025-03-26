from pydantic import BaseModel, Field
from enum import Enum

class ModelName(str, Enum):
    gpt = "gpt"
    gemini = "gemini"

class SegmentName(str, Enum):
    tech = "tech"
    travel = "travel"

class AgentRequest(BaseModel):
    model: ModelName = Field(default=ModelName.gemini, description="LLM model to use (default: gemini)")
    segment: SegmentName = Field(default=SegmentName.tech, description="Content segment (default: tech)")
    topic: str = Field(default="", description="Specific subject matter to generate content about within the chosen segment.")


class PostContent(BaseModel):
    model: ModelName
    segment: SegmentName
    title: str
    content: str
    topic: str
