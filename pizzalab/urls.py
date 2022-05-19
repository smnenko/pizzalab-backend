from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('users/', include('user.urls'), name='users'),
    path('items/', include('item.urls'), name='items'),
    path('categories/', include('category.urls'), name='categories'),

    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="Pizza Lab",
        description="Api documentation for best pizza delivery service ever",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
