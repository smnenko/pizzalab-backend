from django.urls import path, include
from rest_framework import routers

from category.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
