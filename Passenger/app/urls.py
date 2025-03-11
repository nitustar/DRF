from django.urls import path
from .views import passenger_list, passenger_detail

urlpatterns = [
    path('list/', passenger_list, name = 'passenger_list'),
    path('detail/<int:pk>/', passenger_detail, name='passenger_detail'),
]
