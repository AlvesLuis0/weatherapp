from django.db import models

# Create your models here.
class REQUEST(models.Model):
  CITY = models.CharField(max_length=40)
  DATE = models.DateTimeField("Date it was requested")
  
  def __str__(self):
    return self.CITY