from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list(request):
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(reqeust)
    serializer = SnippetSerializer(data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
  """
  Retrieve upadate or delete a particular snippet
  """
  try:
    snippet = Snippet.objects.get(pk=pk)
  except Snippet.DoesNotExist:
    return Response(status=status.HTTP_400_NOT_FOUND)

  if request.method == 'GET':
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data)

  elif resquest.method == 'PUT':
    serializer = SnippetSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serialize.errors, status=400)

  elif request.method == 'DELETE':
    snippet.delete()
    return HttpResponse(status=204)


