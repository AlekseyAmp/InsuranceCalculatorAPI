from tortoise.models import Model
from tortoise import fields

from utils.validators import PositiveNumberValidator


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(max_length=1)
    cargo_type = fields.CharField(max_length=1024)
    rate = fields.FloatField(validators=[PositiveNumberValidator()])
