from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    return render_to_response('index.html')

def academics(request):
    return render_to_response('academics.html')

def contact(request):
    return render_to_response('contact.html')

def placement(request):
    return render_to_response('placement.html')