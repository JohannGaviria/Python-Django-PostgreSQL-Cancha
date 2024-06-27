from rest_framework import serializers
from .models import StatusReservation, Reservation


class StatusReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusReservation
        fields = [
            'id',
            'status'
        ]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id',
            'start_datetime',
            'end_datetime',
            'status',
            'user',
            'court',
        ]
