from django.db import models
from django.conf import settings

# Create your models here.
class Expense(models.Model):
    
    name = models.CharField(max_length=300)
    cost = models.IntegerField()
    category = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
