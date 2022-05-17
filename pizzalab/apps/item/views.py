from rest_framework import generics

from item.models import Item
from item.serializers import ItemDetailSerializer
from item.serializers import ItemSerializer


class BaseItemAPIView(generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListAPIView(generics.ListCreateAPIView, BaseItemAPIView):
    pass


class ItemAPIView(generics.RetrieveUpdateDestroyAPIView, BaseItemAPIView):
    serializer_class = ItemDetailSerializer


