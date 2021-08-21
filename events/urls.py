from django.urls import path

from .views import (EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView,
                    comments_list, comment_detail, EventListViewSet)

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view()),
    path('event/<int:pk>/',EventRetrieveUpdateDestroyAPIView.as_view()),
    path('comments/', comments_list),
    path('comments/<int:pk>/', comment_detail),
    path('event_datetime/', EventListViewSet, name='api_event_datetime'),
]
