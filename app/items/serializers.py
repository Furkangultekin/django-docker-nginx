from django.utils import timezone
from rest_framework import serializers
from .models import Item

#Items serializer
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "category_id", "stock","barcode_num","seller")

    #Create an Item
    def create(self,data):

        return Item.objects.create(**data)

    #Update an item
    def update(self,instance,data):
        for (key,value) in data.items():
            setattr(instance,key,value)
        instance.save()
        return instance

        