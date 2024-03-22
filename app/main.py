from fastapi import FastAPI
from app_statistic.routers.statistic import router as router_statistic

app = FastAPI()

app.include_router(router_statistic)