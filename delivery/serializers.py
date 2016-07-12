from django.contrib.auth.models import User, Group
from rest_framework import serializers
from delivery.models import Pizza, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name', 'price')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    pizzas = serializers.StringRelatedField(many=True)
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = Order
        fields = ('id', 'user', 'pizzas', 'total', 'status')
