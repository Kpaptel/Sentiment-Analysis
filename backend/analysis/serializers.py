from rest_framework import serializers
from .models import SentimentAnalysis


class SentimentAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentAnalysis
        fields = ['id', 'text', 'sentiment', 'created_at']  # Include the fields you want to serialize
