from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Tags, Perspectives, Events
from .serializers import *

@csrf_exempt
@require_http_methods(["POST"])
def endorse(request, pk):
    if request.method == "POST":
        
        try:
            upvote = Perspectives.objects.get(pk=pk)
            upvote.upboat += 1
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
def oppose(request, pk):
    if request.method == "POST":
        
        try:
            upvote = Perspectives.objects.get(pk=pk)
            upvote.downboat += 1
            serializer = PerspectivesSerializer(upvote)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return HttpResponse(status=400)
        except Perspectives.DoesNotExist:
            return HttpResponse(status=404)
