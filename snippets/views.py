from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnipperSerializer

class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSONResponse
  """
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['conent_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return JSONResponse(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(reqeust)
    serializer = SnippetSerializer(data=data)

    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)