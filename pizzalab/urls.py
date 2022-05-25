from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Pizzalab API",
        default_version='v1',
        description="API for best pizza service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="stanichgame@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/users/', include('user.urls'), name='users'),
    path('api/items/', include('item.urls'), name='items'),
    path('api/categories/', include('category.urls'), name='categories'),

    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
