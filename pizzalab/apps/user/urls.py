from django.urls import path
from user import views


urlpatterns = [
    path('', views.UserListCreateView.as_view()),
    path('<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view())
]
