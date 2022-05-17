from django.urls import path

from item.views import ItemListAPIView
from item.views import ItemAPIView

urlpatterns = [
    path('', ItemListAPIView.as_view(), name='list_items'),
    path('<int:pk>/', ItemAPIView.as_view(), name='get_item'),
]
