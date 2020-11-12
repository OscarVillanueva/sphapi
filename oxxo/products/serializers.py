from rest_framework import serializers
from .models import Beer
from .models import Customer
from .models import Order

class BeerSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Beer
        fields = "__all__"

class CustomerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Order
        fields = "__all__"