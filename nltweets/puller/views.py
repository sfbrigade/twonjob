# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from puller import services

# Create your views here.
def webhook(request):
    p = services.TweetPuller()
    p.run_puller()
    return HttpResponse("Yeet!")
