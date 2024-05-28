from uuid import UUID

from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Composition
from .serializers import CompositionSerializer


class CompositionViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class DownloadComposition(APIView):
    def get(self, request, composition_id: UUID):
        try:
            return FileResponse(open(f'./songs/{composition_id}.mp3', 'rb'))
        except FileNotFoundError:
            return Response({'detail': 'Composition not found'}, status=status.HTTP_404_NOT_FOUND)
