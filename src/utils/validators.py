from tortoise.exceptions import ValidationError
from tortoise.validators import Validator


class PositiveNumberValidator(Validator):
    """
    A validator to validate whether the given value is an positive number or not.
    """
    def __call__(self, value: int):
        if value <= 0:
            raise ValidationError(f"Value '{value}' is not an positive number")
