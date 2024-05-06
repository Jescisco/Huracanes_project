from rest_framework import serializers
from .models import Login
# Aqui creamos el json para la api
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        #esto es un ejemplo, aqui estamos creando un json del modelo login.
        model = Login
        fields = '__all__'