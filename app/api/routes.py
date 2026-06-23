from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello from production-style FastAPI"}

@router.get("/health")
def health():
    return {"status": "ok"}