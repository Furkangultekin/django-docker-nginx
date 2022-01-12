from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ItemSerializer
from .models import Item

#Adding Item view
#/add service; POST 
class AddItemView(APIView):
    def post(self,request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#Update Item View
#/Update service;POST
class UpdateItemView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        id = request.data['id']
        qs = Item.objects.filter(id=id).first()
        serializer = ItemSerializer(qs, data=data)

        if qs is None:
            raise NotFound('Item not found')

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)

