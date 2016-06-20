# coding: utf-8
from .models import Feedback, Word
from rest_framework import serializers


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'level', 'score', 'answer')


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('gostei', 'evaluation', 'frase_id')
