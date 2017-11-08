# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from words.models import Word
from words.serializers import WordSerializer


@api_view(['GET'])
def test(request):
	return Response({"message": "Hello world!!!"})


# START HERE, IT PROBABLY DOESNT WORK


@api_view(['GET'])
def word_anagrams(request):
	'''
	list all anagrams for given word
	'''
	word = request.GET.get('word')

	matches = Word.get_anagrams(str(word))
	setup = {'matches': matches}
	return Response(setup)









	# elif request.method == 'POST':
	# 	serializer = WordSerializer(data=request.DATA)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	else:
	# 		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

