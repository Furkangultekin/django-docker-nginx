from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from items.serializers import ItemSerializer
from items.models import Item


#List all items
#/all sevice; GET
class ItemListView(APIView):
    def get(self,request):
        items = Item.objects.all()
        if not items:
            raise NotFound('item not found')
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)

#List items using category id
#/category/:category_id service; GET
class ItemListCatoIdView(APIView):
    def get(self,request,category_id):
        items = Item.objects.filter(category_id=category_id)
        if not items:
            raise NotFound('category not found')
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)

#List items using seller name
#/seller/:seller_name service; GET
class ItemListSellerView(APIView):
    def get(self,request,seller):
        items = Item.objects.filter(seller=seller)
        if not items:
            raise NotFound('seller not found')
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)

#List an item using item name
#/name/:item_name; GET
class ItemListNameView(APIView):
    def get(self,request,itemname):
        items = Item.objects.filter(name=itemname)
        if not items:
            raise NotFound('name not found')
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)


