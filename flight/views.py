from django.shortcuts import render
from .serializers import FlightSerializer,ReservationSerializer
from .models import Flight , Passenger , Reservation
# Create your views here.
from rest_framework import viewsets
from .permission import ItStafforReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (ItStafforReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer