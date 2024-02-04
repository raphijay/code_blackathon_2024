from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Tags, Perspectives, Events
from .serializers import *
from rest_framework.parsers import JSONParser

@csrf_exempt
@require_http_methods(["POST"])
def endorse(request, id):
    if request.method == "POST":
        
        try:
            upvote = Perspectives.objects.get(id=id)
            upvote.upboat += 1
            serializer = PerspectivesSerializer(upvote)
            print(serializer.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return HttpResponse(status=400)
        except Perspectives.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
@require_http_methods(["POST"])
def oppose(request, id):
    if request.method == "POST":
        
        try:
            upvote = Perspectives.objects.get(id=id)
            upvote.downboat += 1
            serializer = PerspectivesSerializer(upvote)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return HttpResponse(status=400)
        except Perspectives.DoesNotExist:
            return HttpResponse(status=404)

@csrf_exempt
@require_http_methods(["POST"])
def addperspective(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PerspectivesSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
@require_http_methods(["POST"])
def addevent(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = EventsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
@require_http_methods(["POST"])
def addtag(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TagsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
@require_http_methods(["GET"])
def getperspectives_all(request):

    if request.method == "GET":
        things = Perspectives.objects.all()
        serializer = PerspectivesSerializer(things, many=True)

        return JsonResponse(serializer.data)
    

@csrf_exempt
@require_http_methods(["GET"])
def getevents_all(request):

    if request.method == "GET":
        things = Events.objects.all()
        serializer = EventsSerializer(things, many=True)

        return JsonResponse(serializer.data)
    
@csrf_exempt
@require_http_methods(["GET"])
def perspective_choice(request, id):

    try:
        perspective = Perspectives.objects.get(pk=id)
    except Perspectives.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PerspectivesSerializer(perspective)
        return JsonResponse(serializer.data)
    

@csrf_exempt
@require_http_methods(["GET"])
def event_choice(request, id):

    try:
        event = Events.objects.get(pk=id)
    except Events.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = EventsSerializer(event)
        return JsonResponse(serializer.data)

