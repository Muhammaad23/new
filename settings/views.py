from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserSettings
from .serializers import UserSettingsSerializer

@api_view(['GET', 'PUT'])
def user_settings(request):
    settings, created = UserSettings.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        serializer = UserSettingsSerializer(settings)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
