from django.urls import path
from . import views  # Ensure views are imported

urlpatterns = [
    path('', views.sentiment_form, name='sentiment_form'),  # Frontend form
    path('analyze/', views.analyze_sentiment_api, name='analyze_sentiment'),  # API endpoint
]
