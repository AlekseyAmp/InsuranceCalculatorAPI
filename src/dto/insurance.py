from pydantic import BaseModel


class Insurance(BaseModel):
    declared_value: float = 500
    cargo_type: str
