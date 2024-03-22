from fastapi import APIRouter, Depends

from app.app_statistic.schemas.statistic import SummStatisticSchema
from app.app_statistic.service import statistic_service
from app.app_statistic.service.statistic_service import StatisticService

router = APIRouter(
    prefix="/statistic",
    tags=["Статистика"]
)


@router.get("/statistics")
async def get_statistics(filter_params: SummStatisticSchema = Depends(),
                         statistic_service: StatisticService = Depends()):
    """
       Get запрос получения общей статистики
    """

    return await statistic_service.get_statistics(**filter_params.model_dump(exclude_none=True))
