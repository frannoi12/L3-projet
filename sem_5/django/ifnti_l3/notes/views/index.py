from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("Bonjour tout le monde !")
	return render(request,"notes/index.html")

