from django.urls import path

from .views import GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView, RatingListAPIView

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view()),
    path('group/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('ratings/', RatingListAPIView.as_view()),
]
