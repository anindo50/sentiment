from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from sentiment_analysis.serializers import SentimentSerializer
        
        

#downloading vader lexicon sentiment analyze tool
nltk.download('vader_lexicon')
#function for take json value as input and retuen the result positive negative neutral
@api_view(['POST'])
def analyze(request):
    if request.method == 'POST':
        data = request.data.get('text', '')
        if not data:
            return Response({'error': "your key should be 'text'"}, status=400)
        if data:
            sid = SentimentIntensityAnalyzer()
            sentiment_scores = sid.polarity_scores(data)
            compound_score = sentiment_scores['compound']

            if compound_score >= 0.05:
                sentiment = 'positive'
            elif compound_score <= -0.05:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
                
            serializer = SentimentSerializer({'sentiment': sentiment})
            return Response(serializer.data)
    else:
        return Response({'error': 'Invalid request method.'}, status=405)


#for not getting error after starting server it will rediract you in analyze page
def hello(request):
    return HttpResponse("<a href='/analyze'>Please click here for sentiment analyze</a>")

