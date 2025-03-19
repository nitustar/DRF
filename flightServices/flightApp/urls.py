from django.urls import path, include

from rest_framework.routers import DefaultRouter
from flightApp.views import *

router = DefaultRouter()

router.register('flights', FlightViewset)
router.register('passengers', PassengerViewset)
router.register('reservations', ReservationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('findFlights/', find_flights),
    path('saveReservation/', save_reservation)
]