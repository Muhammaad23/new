# translator/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from .serializers import TranslationSerializer


class TranslateText(APIView):
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            dest_language = serializer.validated_data['dest_language']

            translator = Translator()
            translated_text = translator.translate(text, dest=dest_language).text

            return Response({'translated_text': translated_text}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
