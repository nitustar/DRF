from django.urls import path
from .views import *

urlpatterns = [
    path('customer/', CustomerListCreate.as_view()),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view()),
    path('order/', OrderListCreate.as_view()),
    path('order/<int:pk>/', OrderRettrieveUpdateDestroy.as_view()),
]