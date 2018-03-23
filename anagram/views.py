from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .find_anagrame import get_word


def find(request, word):
    data = get_word(word)
    if len(data)>1:
        return JsonResponse({"word": data})
    return JsonResponse({"word": []})


def error(request):
    return HttpResponse("error")
