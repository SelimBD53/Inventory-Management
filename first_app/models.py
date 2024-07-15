from django.db import models

# Create your models here.
class ListCompany(models.Model):
   code = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=30)
   
   
def __str__(self):
   return self.name