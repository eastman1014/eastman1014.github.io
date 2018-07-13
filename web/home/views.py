from django.shortcuts import render

def index(request):
	return render( request,'home/index.html')

def contact(request):
	return render ( request, 'home/about.html')

def work(request):
	return render (request, 'home/services.html')

def connect(request):
	return render (request, 'home/contact.html')
	