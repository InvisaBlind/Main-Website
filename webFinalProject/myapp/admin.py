from django.contrib import admin
from myapp.models import course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_rating', 'category')

admin.site.register(course, CourseAdmin)