from fastapi import FastAPI
from .api.routes import router
from .core.config import APP_NAME

app = FastAPI(
    title=APP_NAME,
    version="1.0.0",
    description="Python backend for Agentic SDC Project 3"
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "service": APP_NAME,
        "status": "running",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    from .core.config import HOST, PORT
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
