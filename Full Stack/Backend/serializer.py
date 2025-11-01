
from rest_framework import serializers
from .models import ContactMessage, PredictionRecord

class PredictionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionRecord
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"