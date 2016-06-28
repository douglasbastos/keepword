# coding: utf-8
from .models import Feedback, Word
from rest_framework import serializers, permissions


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'level', 'score', 'answer')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('like', 'evaluation', 'frase_id')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
