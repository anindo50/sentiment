from rest_framework import serializers

class SentimentSerializer(serializers.Serializer):
    sentiment = serializers.CharField()
