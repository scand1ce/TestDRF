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
    item = ItemSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Box
        fields = ['id', 'title', 'item', 'created_at']

        # def update(self, instance, validated_data):
        #     Box.objects.filter(item=instance).delete()
        #     items = validated_data.pop("item")
        #     print(items)
        #     for item_ in items:
        #         id = item_.get("id")
        #         title = item_.get("title")
        #         quantity = item_.get('quantity')
        #         new_item = Item.objects.get(pk=id)
        #         Box(title=title, quantity=quantity, item=new_item).save()
        #
        #     instance.__dict__.update(**validated_data)
        #     instance.save()
        #     return instance

    # def create(self, validated_data):
    #     box = Box.objects.create(
    #         title=validated_data['title']
    #                 )
    #     for item_id in validated_data('item'):
    #         item = Item.objects.get(id=item_id)
    #         box.item.add(item)
    #     box.save()
    # def create(self, validated_data):
    #     items_data = validated_data.pop('item')
    #     print(items_data)
    #     box = Box.objects.create(**validated_data)
    #     print(box)
    #     for item_data in items_data:
    #         Item.objects.create(id=box, **item_data)
    #     return box

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     print(instance.id)
    #     instance.title = validated_data.get('title', instance.title)
    #     print(instance.title)
    #
    #     prepared_items = validated_data.pop('item')
    #     print(prepared_items)
    #
    #     for item_ in prepared_items:
    #
    #         i_title = item_.get('title')
    #         i_quantity = item_.get('quantity')
    #         data_instanse = instance.item.get(title=i_title)
    #         print(data_instanse)
    #         data_instanse.item_ = i_title
    #         data_instanse.item_ = i_quantity
    #
    #         instance.item.update()
    #     return instance
