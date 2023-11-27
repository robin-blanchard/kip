from tortoise.models import Model
from tortoise import fields


class User(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    hashed_password = fields.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        table = "users"
