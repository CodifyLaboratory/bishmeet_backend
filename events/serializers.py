from rest_framework.serializers import ModelSerializer

from .models import Comment, Rating, Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'group', 'name', 'location', 'description',
                  'event_date', 'event_time', 'pictures')


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'group', 'name', 'location', 'description',
            'event_date', 'event_time', 'pictures', 'active'
        )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
