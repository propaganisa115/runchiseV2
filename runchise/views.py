# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Restaurant
from django.db.models import Q
from .serializers import RestaurantSerializer

from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

def filter_if_not_none(qs, **kwargs):
        return qs.filter(**{k: v for k, v in kwargs.items() if v is not None})

class RestaurantRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantSearch(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    

    def get_queryset(self):
        if 'name' or 'address' or 'email' or 'phone_number' in self.request.GET:
            queryset = Restaurant.objects.order_by('-name')
            return filter_if_not_none(queryset,
                name=self.request.GET.get('name'),
                address=self.request.GET.get('address'),
                email=self.request.GET.get('email'),
                phone_number=self.request.GET.get('phone_number'),
            )
        else:
            return Restaurant.objects.all()
            