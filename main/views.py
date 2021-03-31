from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return 	render(request,'main/index.html')
def about(request):
	return render(request,'about/about.html')
def download(request):		
    return render(request,'download/download.html')
def sign_in(request):		
    return render(request,'sign_in/sign_in.html')
def sign_up(request):		
    return render(request,'sign_up/sign_up.html')