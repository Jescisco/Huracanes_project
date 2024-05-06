from rest_framework import viewsets
from .serializer import LoginSerializer
from .models import Login

# Create your views here.

class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Login.objects.all()