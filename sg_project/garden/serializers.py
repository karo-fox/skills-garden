from rest_framework import serializers

from .models import Field, Topic

class FieldSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    last_reviewed = serializers.DateField(read_only=True)

    class Meta:
        model = Field
        fields = ['name', 'description', 'review_frequency', 'last_reviewed', 'url']


class TopicSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Topic
        fields = '__all__'