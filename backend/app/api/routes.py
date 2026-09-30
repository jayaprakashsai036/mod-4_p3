from fastapi import APIRouter
from ..models.chat import ChatRequest, ChatResponse, HealthResponse
from ..services.agent import Agent
from ..services.memory import MemoryStore
from ..core.config import MEMORY_FILE

router = APIRouter()
memory = MemoryStore(MEMORY_FILE)
agent = Agent(memory)

@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok")

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply, history_length = agent.process(
        request.session_id,
        request.message
    )
    return ChatResponse(
        reply=reply,
        history_length=history_length
    )
