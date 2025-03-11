from fastapi import APIRouter
# from src.config import settings

router = APIRouter(prefix="", tags=["Health"])


@router.get("/health")
async def read_example():
    return {"message": "Everything is OK   ദ്ദി(>ᴗ•)"}
