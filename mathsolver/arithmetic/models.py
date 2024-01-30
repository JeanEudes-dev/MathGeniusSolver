from django.db import models

class ArithmeticHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    