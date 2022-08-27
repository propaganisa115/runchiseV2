from runchise import views 
from django.urls import path, include
 
urlpatterns = [ 
    path('restaurant', views.RestaurantListView.as_view(), name='list_restaurant'),
    path('restaurant/create', views.RestaurantCreateView.as_view(),name='create_restaurant'),
    path('restaurant/<int:pk>', views.RestaurantRetrieveUpdateView.as_view(),name='retrieve_update_restaurant'),
    path('restaurant/search', views.RestaurantSearch.as_view(),name='search_restaurant'),
    
]
