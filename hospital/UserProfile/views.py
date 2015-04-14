#coding: utf-8
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import viewsets, serializers
from .models import CustomUser

# Create your views here.
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        
        # which can get, post
        fields = ('username', 'password', 'description', 'scope', 'is_active', 'is_staff')
        
class CustomUserViewsets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer