from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user import views


urlpatterns = [
    path('', views.UserListCreateView.as_view(), name='users'),
    path('<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user'),

    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]
