# translator/serializers.py
from rest_framework import serializers

class TranslationSerializer(serializers.Serializer):
    text = serializers.CharField()
    dest_language = serializers.CharField(max_length=10)  # Maqsadli til (masalan, 'fr' yoki 'uz')
