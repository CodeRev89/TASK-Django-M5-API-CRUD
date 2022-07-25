from rest_framework import serializers

from .models import Booking, Flight


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "price", "time", "destination"]


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "date", "flight", "passengers"]

class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields = ["id", "date", "flight", "passengers"]
class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields =["passengers", "date"]
class BookingDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields= "__all__"