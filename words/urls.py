from django.conf.urls import url
from django.contrib import admin

from words.views import test, word_anagrams



urlpatterns = [
    url(r'^hello/', test, name='test'),
    url(r'^anagrams/', word_anagrams, name='word_anagrams'),
    
]