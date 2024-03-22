from fastapi import APIRouter

router = APIRouter(
    prefix="/statistic",
    tags=["Стастика"]
)


@router.get("")
async def get_statistic():
    return {"code": 200, "msg": "ok"}
