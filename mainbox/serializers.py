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


class BoxSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    item = ItemSerializer(many=True, read_only=False)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Box
        fields = ['id', 'title', 'item', 'created_at']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        prepared_items = validated_data.pop('item')
        print(prepared_items)

        for item_ in prepared_items:
            i_title = item_.get('title')
            print(i_title)

            i_quantity = item_.get('quantity')
            print(i_quantity)
            instance.save()
            return instance

