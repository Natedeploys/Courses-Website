from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    # returns a string
    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    # creates steps to be related to a single course
    course = models.ForeignKey(Course)

    # controls how model does some stuff
    class Meta:
        ordering = ['order',]


    # returns a string
    def __str__(self):
        return self.title