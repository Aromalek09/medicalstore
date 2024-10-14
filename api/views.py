from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.serializers import UserSerializer,AddMedicineSerializer,OrderSerializer
from api.models import AddMedicine,Order

# Create your views here.


class UserView(ModelViewSet):
    
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
class UserCreationViewset(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
    
class MedicineModelViewset(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=AddMedicineSerializer
    queryset=AddMedicine.objects.all()
    
class OrderModelViewset(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    