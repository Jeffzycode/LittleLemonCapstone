from django.test import TestCase, Client
from django.utils import timezone
from restaurant.models import MenuItem, Booking
from littlelemonapi.serializers import MenuSerializer, BookingSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='customer',
            password='123'
        )
        MenuItem.objects.create(title="Falafel", price=60, inventory=200)
        MenuItem.objects.create(title="Tacos", price=40, inventory=7)
    def test_getall(self):
        self.setup()
        # Run Serializer
        serialized_set = MenuSerializer(MenuItem.objects.all(), many=True)
        # Fetch objects from database
        self.assertTrue(self.client.login(username='customer', password='123')) # Login
        response = self.client.get("/restaurant/api/menu/") # Fetch data
        self.assertEqual(response.data, serialized_set.data)

class BookingViewTest(TestCase):
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='customer',
            password='123'
        )
        Booking.objects.create(name="John", no_of_guests=10, booking_date=timezone.now())
        Booking.objects.create(name="Jack", no_of_guests=3, booking_date=timezone.now())
    def test_getall(self):
        self.setup()
        serialized_set = BookingSerializer(Booking.objects.all(), many=True)
        self.assertTrue(self.client.login(username='customer', password='123')) # Login
        response = self.client.get("/restaurant/api/bookings/tables/") # Fetch data
        self.assertEqual(response.data, serialized_set.data)