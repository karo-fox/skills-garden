from rest_framework import serializers

from .models import Field, Topic


class FieldSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    last_reviewed = serializers.DateField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Field
        fields = '__all__'

    def create(self, validated_data):
        field = Field(name=validated_data['name'], description=validated_data['description'],
                      review_frequency=validated_data['review_frequency'],
                      owner=self.context['request'].user)
        field.save()
        return field


class TopicSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    last_reviewed = serializers.DateField(read_only=True)
    field = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

    def create(self, validated_data):
        topic = Topic(name=validated_data['name'], description=validated_data['description'],
                      field=Field.objects.get(id=self.context['view'].kwargs['field_pk']))
        topic.save()
        return topic
