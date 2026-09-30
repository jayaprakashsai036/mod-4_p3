from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1, max_length=120)
    message: str = Field(min_length=1, max_length=5000)

class ChatResponse(BaseModel):
    reply: str
    history_length: int

class HealthResponse(BaseModel):
    status: str
