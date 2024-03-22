from pydantic import BaseModel

from app.app_statistic.models.enum import DepartmentsEnum


class StatisticSchema(BaseModel):
    department: DepartmentsEnum
    mass: int
    personal: int
    informational: int
    survey: int
    commercial_survey: int
    service: int

class DepartmentSchema(BaseModel):
    mass: int
    personal: int
    informational: int
    survey: int
    commercial_survey: int
    service: int

class DepartmentDetailSchema(DepartmentSchema):
    department: dict[DepartmentSchema]