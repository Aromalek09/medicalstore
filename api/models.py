from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AddMedicine(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveBigIntegerField()
    description=models.CharField(max_length=50)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='image',null=True)
    
    def __str__(self) -> str:
        return self.medicine
    
    def answers(self):
        qs=self.order_set.all()
        return qs
    

class Order(models.Model):
    itemname=models.CharField(max_length=100)
    quantity=models.PositiveBigIntegerField()
    date_time=models.DateTimeField(auto_now_add=True)
    
    

    