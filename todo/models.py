from django.db import models

class Categoty(models.Model):
    name= models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    parent_catigory=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)

    created_at=models.DateField(auto_now_add=True)
    created_at=models.DateField(auto_now=True)

    def _str_(self):
       return self.name
    
    def save(self, *args, **kwars):
        print('salom')
    


       
    
# Create your models here.
