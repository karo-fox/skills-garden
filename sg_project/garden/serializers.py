from rest_framework import serializers

from .models import Field, Topic

class FieldSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    last_reviewed = serializers.DateField(read_only=True)


    class Meta:
        model = Field
        fields = ['name', 'description', 'review_frequency', 'last_reviewed', 'url']



class TopicSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    last_reviewed = serializers.DateField(read_only=True)
    field = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Topic
        fields = ['name', 'description', 'field', 'last_reviewed', 'url']
    

    def create(self, validated_data):
        topic = Topic(name=validated_data['name'], description=validated_data['description'],
                      field=Field.objects.get(id=self.context['view'].kwargs['pk']))
        topic.save()
        return topic