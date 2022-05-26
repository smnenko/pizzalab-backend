from rest_framework import generics

from core.permissions import BaseItemPermission
from item.models import Item
from item.serializers import ItemUpdateSerializer
from item.serializers import ItemSerializer


class BaseItemAPIView(generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListAPIView(generics.ListCreateAPIView, BaseItemAPIView):
    permission_classes = (BaseItemPermission,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemUpdateSerializer
        return super().get_serializer_class()


class ItemAPIView(generics.RetrieveUpdateDestroyAPIView, BaseItemAPIView):
    serializer_class = ItemUpdateSerializer
    permission_classes = (BaseItemPermission,)


