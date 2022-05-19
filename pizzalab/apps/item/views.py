from rest_framework import generics

from core.permissions import BaseItemPermission
from item.models import Item
from item.serializers import ItemDetailSerializer
from item.serializers import ItemSerializer


class BaseItemAPIView(generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListAPIView(generics.ListCreateAPIView, BaseItemAPIView):
    permission_classes = (BaseItemPermission, )


class ItemAPIView(generics.RetrieveUpdateDestroyAPIView, BaseItemAPIView):
    serializer_class = ItemDetailSerializer
    permission_classes = (BaseItemPermission, )


