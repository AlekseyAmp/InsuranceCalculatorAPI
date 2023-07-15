from fastapi import HTTPException

from models.rate import Rate
from dto.insurance import Insurance as InsuranceDTO
from utils.dto import check_data_on_empty
from constants import MIN_VALUE, MAX_VALUE, FIRST_DAY_OF_CURRENT_MONTH


async def calculate_insurance(data: InsuranceDTO) -> dict:
    """
    Calculates the insurance cost based on the provided data.

    Args:
        data (InsuranceDTO): The data containing the cargo type and declared value.

    Returns:
        dict: A dictionary with the calculated insurance cost.
    """
    if not check_data_on_empty(data):
        raise HTTPException(
            status_code=400,
            detail="One or more field(s) is empty"
        )

    if data.declared_value <= 0:
        raise HTTPException(
            status_code=400,
            detail="Declared value must be greater than 0"
        )

    if data.declared_value < MIN_VALUE or data.declared_value > MAX_VALUE:
        raise HTTPException(
            status_code=400,
            detail="Declared value must be between 500 and 1 million"
        )

    db_rate = await Rate.filter(
        date=FIRST_DAY_OF_CURRENT_MONTH,
        cargo_type=data.cargo_type
    ).first()

    if not db_rate:
        raise HTTPException(
            status_code=404,
            detail="Enter one of the suggested cargo-type - [Electronics, Furniture, Chemicals, Other]"
        )

    cost_insurance = db_rate.rate * data.declared_value

    return {
        "cost_insurance": round(cost_insurance, 3)
    }
