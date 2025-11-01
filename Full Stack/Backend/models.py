
from django.db import models

class PredictionRecord(models.Model):
    input_data = models.JSONField()
    result = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id} at {self.created_at}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"