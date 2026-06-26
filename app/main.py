from fastapi import FastAPI
from app.api.v1.router import internal_router
app = FastAPI(
    title="Nursery API",
    version="0.1.0",
    description="API for the Nursery business."
)

app.include_router(internal_router)

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "statusCode": 200
    }