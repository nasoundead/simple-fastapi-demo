from fastapi import APIRouter

router = APIRouter()


@router.get('/index', tags=["myorder"])
async def readOrders():
    return {"message": "allorders"}
