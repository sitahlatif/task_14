
from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer
# Your imports should be here


# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	