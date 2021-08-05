from rest_framework import serializers

from .models import TextSource, URLSource

from garden.models import Topic


class TextSourceSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TextSource
        fields = '__all__'

    def create(self, validated_data):
        source = TextSource(name=validated_data['name'], content=validated_data['content'],
                            topic=Topic.objects.get(id=self.context['view'].kwargs['topic_pk']))
        source.save()
        return source


class URLSourceSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = URLSource
        fields = '__all__'

    def create(self, validated_data):
        source = URLSource(name=validated_data['name'], content=validated_data['content'],
                           topic=Topic.objects.get(id=self.context['view'].kwargs['topic_pk']))
        source.save()
        return source
