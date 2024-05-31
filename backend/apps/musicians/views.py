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
