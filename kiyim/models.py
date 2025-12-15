from django.db import models



class Kurtka(models.Model):
    nami= models.CharField(max_length=200)
    brend=models.CharField(max_length=200)
    rang=models.CharField(max_length=200)
    narxi=models.DecimalField(decimal_places=2, max_digits=10)
    skidka=models.IntegerField(default=0)

    def __str__(self):
        return self.nami

# Create your models here.

class Futbolka(models.Model):
    nami= models.CharField(max_length=200)
    davlat=models.CharField(max_length=200)
    brend=models.CharField(max_length=200)
    rang=models.CharField(max_length=200)
    narxi=models.DecimalField(decimal_places=2, max_digits=10)
    skidka=models.IntegerField(default=0)
    sotuvdagi_soni=models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.nami
    
class Telefon (models.Model):
    class RamChoices(models.TextChoices):
        black= 'gb4','4 Gb'
        white='gb8' ,'8 Gb'

    class ColorChoices(models.TextChoices):
        black= 'qora','Qora'
        white = 'oq' , 'Oq'
        red = 'qizil' , 'Qizil'

    class BrendChoices(models.TextChoices):
        samsung = 'samsung' , 'Samsung'
        iphone = 'iphone' , 'Iphone'

    narxi=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/')
    color = models.CharField(max_length=30, choices=ColorChoices.choices )
    brend =models.CharField(max_length=30, choices=BrendChoices.choices)
    ram=models.CharField(max_length=30 , choices=RamChoices.choices)   
        
    
def __str__(self):
        return self.brend
