from rest_framework import serializers
from api.models import AddMedicine,Order
from django.contrib.auth.models import User








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        
    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
    
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username"]
    

class AddMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddMedicine
        fields="__all__"
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
