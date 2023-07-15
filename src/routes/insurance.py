from fastapi import APIRouter

from services import insurance as InsuranceService
from dto.insurance import Insurance as InsuranceDTO


router = APIRouter()


@router.post("/insurance/calculate")
async def calculate_insurance(data: InsuranceDTO):
    return await InsuranceService.calculate_insurance(data)
