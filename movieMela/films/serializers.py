from rest_framework import serializers
from .models import Films
from django.contrib.auth.models import User


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'