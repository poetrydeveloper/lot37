from pydantic import BaseModel

from app.app_statistic.models.enum import DepartmentsEnum


class CreatedStatisticSchema(BaseModel):
    department: DepartmentsEnum
    mass: int
    personal: int
    informational: int
    survey: int
    commercial_survey: int
    service: int


class StatisticSchema(BaseModel):
    mass: int
    personal: int
    informational: int
    survey: int
    commercial_survey: int
    service: int


class DepartmentDetailSchema(StatisticSchema):
    marketing: StatisticSchema
    sales: StatisticSchema
    informational: StatisticSchema
    survey: StatisticSchema
    commercial_survey: StatisticSchema
    service: StatisticSchema


class SummStatisticSchema(BaseModel):
    total: StatisticSchema
    departments: DepartmentDetailSchema
