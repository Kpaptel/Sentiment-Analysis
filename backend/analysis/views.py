from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer
from transformers import pipeline
from .forms import SentimentForm

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def sentiment_form(request):
    sentiment = None
    form = SentimentForm()  # Create an instance of the form

    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']  # Get the validated data
            sentiment = analyze_sentiment(text)  # Call the analyze_sentiment function

    return render(request, 'analysis/sentiment_form.html', {'form': form, 'sentiment': sentiment})

@api_view(['POST'])
def analyze_sentiment_api(request):
    text = request.data.get('text')
    
    if not text:
        return Response({"error": "Text is required."}, status=status.HTTP_400_BAD_REQUEST)

    result = sentiment_pipeline(text)
    sentiment = SentimentAnalysis.objects.create(text=text, sentiment=result[0]['label'])

    serializer = SentimentAnalysisSerializer(sentiment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def analyze_sentiment(text):
    # Call the sentiment pipeline and return the result
    result = sentiment_pipeline(text)
    return result[0]['label']  # Return the sentiment label
