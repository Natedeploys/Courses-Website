from django.shortcuts import get_object_or_404, render

# look inside the current dir for models
from .models import Course, Step


# Create your views here.
def course_list(request):
    # Gets all the stuff in the db
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# we provide an primary key through the url to get the course
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
