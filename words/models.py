# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Word(models.Model):

	title = models.CharField(max_length=60)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

	@staticmethod
	def get_all_words():
		return [i.title for i in Word.objects.all()]
		
	@classmethod
	def get_anagrams(cls, word):
		winners = []
		for choice in Word.get_all_words():
			if sorted(choice) == sorted(word):
				winners.append(choice)
		return [j for j in winners if j != word]

	