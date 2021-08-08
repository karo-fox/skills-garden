from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords aren't matching")
        return data
