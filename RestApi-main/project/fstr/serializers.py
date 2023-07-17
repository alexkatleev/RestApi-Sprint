from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        verbose_name = 'Уровень сложности'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        verbose_name = 'Пользователь'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        verbose_name = 'Изображение'


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'


class PerevalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
        read_only_fields = ['user', ]
