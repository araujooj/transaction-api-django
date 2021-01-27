from django.db import models


class Transaction(models.Model):
    title = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    value = models.FloatField()
    category = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
