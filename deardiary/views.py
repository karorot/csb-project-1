from django.shortcuts import render
from django.http import HttpResponse


def diaryView(request, user_id):
    response = "Diary for user %s"
    return HttpResponse(response % user_id)

def entryReadView(request, entry_id):
    response = "Entry %s"
    return HttpResponse(response % entry_id)

def entryCreateView(request):
    response = "Write a new diary entry"
    return HttpResponse(response)

def homePageView(request):
    return HttpResponse("Hello, world. This is index.")
