from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

import json

from models import (Student, StudentClass)


def index(request):
    """
    """
    return HttpResponse("Hello, world. You're at the polls index.")


class StudentView(View):
    """ StudentView View
        We only defined a get request method here. 
        We can expand on this and build a full RESTful view.
    """

    def get(self, request):
        """ Get method for students endpoint
            - parameters 
                first: 
                last:
                email:
                average_gpa:
            - returns: {'students': [<students>], 'classes': [<classes>]}
        """
        first = request.GET.get("first", None)
        last = request.GET.get("last", None)
        email = request.GET.get("email", None)
        average_gpa = request.GET.get("average_gpa", None)

        data = {"students": [], "classes": []}

        for student in Student.objects.all():
            data["students"].append(student.to_dict())

        for student_class in StudentClass.objects.all():
            data["classes"].append(student_class.to_dict())

        return HttpResponse(json.dumps(data))
