import math
from django.db import models

class AlgebraHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.expression + "=" + str(self.result)
    

class ArithmeticHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.expression + "=" + str(self.result)
    
class CalculusHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.expression + ": " + str(round(float(self.result), 5))
    
class DifferentialEquationHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.expression} | {round(float(self.result),4)} at t={self.timestamp}"
    
class LinearAlgebraHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.expression} | {round(float(self.result),4)} at t={self.timestamp}"
    
class TrigonometryHistory(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.expression}: {round(math.degrees(float(self.result)),2)}° @ {self.timestamp}"

