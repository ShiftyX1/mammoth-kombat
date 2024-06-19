from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    score = fields.IntField(default=0)

    def __str__(self):
        return self.username
