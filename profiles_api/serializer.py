from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API view"""
    #validation rule - corret type for that field
    name = serializers.CharField(max_length = 10)
