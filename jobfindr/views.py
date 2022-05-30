from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "jobfindr/index.html")

def hello(request):
    if request.method == "GET":
        return JsonResponse({'msg': 'Hello world! as JSON'})