from rest_framework import serializers

class TranslationSerializer(serializers.Serializer):
    text = serializers.CharField()
    dest_language = serializers.ChoiceField(choices=['uz', 'en', 'ru'])  # Faqat ushbu tillar ruxsat etiladi
