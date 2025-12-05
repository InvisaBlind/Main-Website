from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def project(request):
    return render(request, "project.html")
def comingsoon(request):
    return render(request, "comingsoon.html")
def onlineLearningPlatform(request):
    return render(request, "onlineLearningPlatform.html")