from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Favorite(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    topics = JSONField()

    class Meta:
        db_table = "favorite"