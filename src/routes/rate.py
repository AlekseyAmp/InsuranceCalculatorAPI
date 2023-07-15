from fastapi import APIRouter

from services import rate as RateService


router = APIRouter()


@router.post("/rates/upload")
async def upload_rates_from_json():
    return await RateService.upload_rates_from_json()


@router.patch("/rates/update")
async def update_rates_from_json():
    return await RateService.update_rates_from_json()
