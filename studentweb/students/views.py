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
    """
    """

    def get(self, request):
        """
        """
        data = {"students": [], "classes": []}

        for student in Student.objects.all():
            data["students"].append(student.to_dict())

        for student_class in StudentClass.objects.all():
            data["classes"].append(student_class.to_dict())

        return HttpResponse(json.dumps(data))
