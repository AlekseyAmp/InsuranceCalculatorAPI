from fastapi import HTTPException
import json
import os
from datetime import datetime
from models.rate import Rate
from constants import JSON_FILE_PATH


async def get_rates() -> list:
    """
    Retrieves all rates from the database.

    Returns:
        list: A list of rates.
    """
    rates = await Rate.all()
    return rates


async def upload_rates_from_json() -> dict:
    """
    Uploads rates from a JSON file to the database.

    Returns:
        dict: A dictionary with a success message.
    """
    if not os.path.exists(JSON_FILE_PATH):
        raise HTTPException(
            status_code=404,
            detail="File path not found"
        )

    rates = await get_rates()
    if rates:
        raise HTTPException(
            status_code=409,
            detail="All data is already loaded"
        )

    try:
        with open(JSON_FILE_PATH) as file:
            data = json.load(file)
            for date_str, rates_list in data.items():
                date = datetime.strptime(date_str, "%Y-%m-%d")
                for rate in rates_list:
                    cargo_type = rate['cargo_type']
                    rate_value = rate['rate']

                    await Rate.create(
                        date=date,
                        cargo_type=cargo_type,
                        rate=rate_value
                    )
    except Exception as e:
        raise Exception(
            "Error occurred while updating rates from JSON file"
        ) from e

    return {
        "message": "Data uploaded successfully"
    }


async def update_rates_from_json() -> dict:
    """
    Updates rates from a JSON file in the database.

    Returns:
        dict: A dictionary with a success message.
    """
    if not os.path.exists(JSON_FILE_PATH):
        raise HTTPException(
            status_code=404,
            detail="File path not found"
        )

    try:
        with open(JSON_FILE_PATH) as file:
            data = json.load(file)
            for date_str, rates_list in data.items():
                date = datetime.strptime(date_str, "%Y-%m-%d")
                for rate in rates_list:
                    cargo_type = rate['cargo_type']
                    rate_value = rate['rate']

                    db_rate = await Rate.filter(
                        date=date,
                        cargo_type=cargo_type
                    ).first()

                    if db_rate:
                        if db_rate.rate != rate_value:
                            db_rate.rate = rate_value
                            await db_rate.save()
                    else:
                        await Rate.create(
                            date=date,
                            cargo_type=cargo_type,
                            rate=rate_value
                        )
    except Exception as e:
        raise Exception(
            "Error occurred while updating rates from JSON file"
        ) from e

    return {
        "message": "Data updated successfully"
    }
