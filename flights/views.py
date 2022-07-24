from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer, BookingDetailsSerializer, BookingUpdateSerializer, BookingDestroySerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
    lookup_field="id"
    lookup_url_kwarg= "booking_id"

class BookingDetailsView(RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingDetailsSerializer
    lookup_field="id"
    lookup_url_kwarg="booking_id"

class BookingUpdateViews(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

class BookingDestroyViews(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDestroySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'