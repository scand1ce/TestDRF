from rest_framework import serializers
from .models import Item, Box, Discr


class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discr
        fields = ['id', 'description']


class ItemSerializer(serializers.ModelSerializer):
    description = CharacteristicsSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'quantity', 'description']
        nested_proxy_field = True


class BoxSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Box
        fields = [
            'id',
            'title',
            'item',
            'created_at'
        ]
