from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
# Create your views here.

def talkList(request):
    return HttpResponse('To Do List')