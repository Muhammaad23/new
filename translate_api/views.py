from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from .serializers import TranslationSerializer


class TranslateText(APIView):
    allowed_languages = ['uz', 'en', 'ru']  # Faqat shu tillar

    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            dest_language = serializer.validated_data['dest_language']

            if dest_language not in self.allowed_languages:
                return Response(
                    {"error": "Faqat 'uz', 'en', 'ru' tillariga tarjima qilish mumkin."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            translator = Translator()
            translated_text = translator.translate(text, dest=dest_language).text

            return Response({'translated_text': translated_text}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
