from fastapi import APIRouter

agent_router = APIRouter()

@agent_router.get("/")
async def root():
    return {"message":"Hello World"}

