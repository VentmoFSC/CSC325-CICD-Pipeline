from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of my Django application.</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of my Django application.</p>")

@api_view(['GET'])
def api_status(request):
    return Response({
        "status": "success",
        "message": "CSC325 CI/CD Pipeline API is running"
    })
