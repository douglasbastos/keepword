# coding: utf-8
import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from .serializers import FeedbackSerializer, WordSerializer
from .models import Feedback, Word


@api_view()
def next_question(request):
    word = Word.objects.order_by('?').first()
    serializer = WordSerializer([word])
    return Response(serializer.data)


@api_view()
def result_question(request):
    return Response({"message": "Hello, world!"})


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-id')
    serializer_class = FeedbackSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('-id')
    serializer_class = WordSerializer
