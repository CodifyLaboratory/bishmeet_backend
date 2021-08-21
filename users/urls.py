from django.urls import path, include

from .views import UsersListAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('users/', UsersListAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
