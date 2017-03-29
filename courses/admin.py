from django.contrib import admin

# Register your models here.
from .models import Course, Step


class StepInLine(admin.StackedInline):
    model = Step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInLine]


admin.site.register(Course, CourseAdmin)
admin.site.register(Step)

