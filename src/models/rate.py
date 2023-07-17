from tortoise.models import Model
from tortoise import fields

from utils.validators import PositiveNumberValidator


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField
    cargo_type = fields.CharField(max_length=256)
    rate = fields.FloatField(validators=[PositiveNumberValidator()])
