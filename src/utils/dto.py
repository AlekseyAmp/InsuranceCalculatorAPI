from pydantic import BaseModel


def check_data_on_empty(data: BaseModel):
    """
    Checks if any field in the provided data object is empty.

    Args:
        data (BaseModel): The data object to check for empty fields.

    Returns:
        bool: True if all fields have non-empty values, False otherwise.
    """
    for field in data.model_fields:
        value = getattr(data, field)
        if not value:
            return False
    return True
