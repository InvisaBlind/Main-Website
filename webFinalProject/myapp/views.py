from django.shortcuts import render
from myapp.models import course

# Create your views here.
def home(request):
    return render(request, "home.html")
def courses(request):
    course_list = course.objects.all()
    return render(request, "courses.html", {"courses": course_list})
def about(request):
    return render(request, "about.html")
def lesson(request):
    return render(request, "lesson.html")