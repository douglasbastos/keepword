# coding: utf-8

from rest_framework import viewsets
from core.models import Feedback, Word
from .serializers import FeedbackSerializer, WordSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-id')
    serializer_class = FeedbackSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('-id')
    serializer_class = WordSerializer
