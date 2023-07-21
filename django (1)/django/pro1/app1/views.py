from django.shortcuts import render
from django.http import HttpResponse,HttpRequest


# Create your views here.
def home1(request):
	return render(request,'home.html')