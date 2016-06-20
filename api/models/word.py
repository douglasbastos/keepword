# coding: utf-8

from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=140)
    level = models.IntegerField()
    score = models.DecimalField(max_digits=12, decimal_places=2)
    answer = models.CharField(max_length=140)

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self):
        return self.word
