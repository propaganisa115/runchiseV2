from rest_framework import serializers 
from runchise.models import Restaurant
 
 
class RestaurantSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Restaurant
        fields = ('id',
                  'name',
                  'phone_number',
                  'address',
                  'email')
