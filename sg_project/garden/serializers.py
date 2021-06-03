from rest_framework import serializers

from .models import Field, Topic

class FieldSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Field
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Topic
        fields = '__all__'