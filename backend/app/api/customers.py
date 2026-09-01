from fastapi import APIRouter
router = APIRouter(prefix="/customers")
@router.get("/")
async def list_customers():
    return [{"id": "1", "name": "John Doe"}]
