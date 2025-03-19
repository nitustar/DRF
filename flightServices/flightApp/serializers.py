from rest_framework import serializers
from .models import Flight, Passenger, Reservation

import re

def validate_data(data):                    # Custom validator function -> that can be used for validating data fields for any serializer
    print(data)
    return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [validate_data]

    def validate(self, data):           # Custom validator function -> that can be used for validate multiple data fields
        if re.match("^[a-zA-Z0-9]*$", data['flight_number'])==None:
            raise serializers.ValidationError("Invalid flight number. Make sure it contains only alphanumeric characters.")
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'