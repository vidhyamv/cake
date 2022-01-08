from django.db import models

# Create your models here.
class Cake(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    prize=models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.name




