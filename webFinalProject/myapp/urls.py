from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("course/", views.courses, name="courses"),
    path("about/", views.about, name="about"),
    path("lesson/", views.lesson, name="lesson"),
]