# coding: utf-8

from django.db import models
from .word import Word


class Feedback(models.Model):
    gostei = models.BooleanField()
    evaluation = models.IntegerField(null=True)
    frase_id = models.ForeignKey(Word)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
