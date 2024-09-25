from django.db import models

class SentimentAnalysis(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text