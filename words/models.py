# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Word(models.Model):
	title = models.CharField(max_length=60)


	def __str__(self):
		return self.title


