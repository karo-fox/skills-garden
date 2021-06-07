from rest_framework import serializers

from .models import TextSource, URLSource

class TextSourceSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = TextSource
        fields = '__all__'
    


class URLSourceSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = URLSource
        fields = '__all__'