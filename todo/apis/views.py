from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from todomain import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.TodoItems.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoItems.objects.all()
    serializer_class = TodoSerializer
