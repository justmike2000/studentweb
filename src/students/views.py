# -*- coding: utf-8 -*-
"""Views for students Django App
"""

import json
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View

from students.models import (Student, StudentClass)


def index(request):
    """Endpoint will return a rendered template of student_views.html.
    """
    template = loader.get_template('view_students.html')
    return HttpResponse(template.render({}, request))

class StudentView(View):
    """ StudentView View
        We only defined a get request method here.
        We can expand on this and build a full RESTful view.
    """

    def get(self, request):
        """ Get method for students endpoint
            - parameters
                first: Filter by first name
                last: Filter by last name
                average_gpa: Filter by average gpa
            - returns: {'students': [<students>], 'classes': [<classes>]}
        """
        first = request.GET.get("first", None)
        last = request.GET.get("last", None)
        average_gpa = request.GET.get("average_gpa", None)

        students = Student.objects

        if first is not None:
            students = students.filter(first_name__contains=first)
        if last is not None:
            students = students.filter(last_name__contains=last)

        data = {"students": [], "classes": []}

        for student in students.all():
            if average_gpa is not None and round(student.average_gpa, 1) != round(float(average_gpa), 1):
                continue
            data["students"].append(student.to_dict())

        for student_class in StudentClass.objects.all():
            data["classes"].append(student_class.to_dict())

        return HttpResponse(json.dumps(data))
