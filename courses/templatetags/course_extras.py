from django import template
from django.utils.safestring import mark_safe
from courses.models import Course
import markdown2

# instantiated the library class
register = template.Library()


# Registers a function as a simple tag.
# Simple tags don't include new templates,
# don't have an end tag, and don't assign
# values to context variables.
@register.simple_tag
def newest_course():
    '''
    Gets the most recent course that was added to the library'''
    return Course.objects.latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''returns dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}


# custom filters
@register.filter('time_estimate')
def time_estimate(word_count):
    '''estimates the number of minutes a course step takes
    to complete based on the word count'''
    minutes = round(word_count/2)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)