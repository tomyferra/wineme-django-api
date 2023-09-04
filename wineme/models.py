from django.db import models
import datetime

# Create your models here.
#change
class Wine(models.Model):
    Name = models.CharField(max_length=500)
    Winery = models.CharField(max_length=500)
    Variety = models.CharField(max_length=500)
    Image = models.CharField(max_length=500)
    Region = models.CharField(max_length=500)
    Description = models.CharField(max_length=1000)
    Year = models.IntegerField(default=datetime.datetime.today().year)
    Totalqualifications = models.IntegerField(default=0)
    Avgqualifications = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    Score = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def _str_(self):
        return self.Name
