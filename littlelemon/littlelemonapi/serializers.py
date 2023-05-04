from rest_framework.serializers import ModelSerializer
from restaurant.models import MenuItem, Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"