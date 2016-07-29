# -*- coding: utf-8 -*-
"""Django Tests
"""

import json
from django.test import RequestFactory
from django.test import TestCase

from students.models import (Student, StudentClass, Semester)
from students.views import StudentView

class StudentTestCase(TestCase):
    """Tests Class methods and proprties of students and views
    """

    def setUp(self):
        sone = Student.objects.create(first_name="First Name",
                                      last_name="Last Name",
                                      email="email@example.com")
        stwo = Student.objects.create(first_name="Bobby",
                                      last_name="Smith",
                                      email="bobbysmith@example.com")

        cone = StudentClass.objects.create(description="Math 101")
        ctwo = StudentClass.objects.create(description="Math 201")
        cthree = StudentClass.objects.create(description="English 101")

        Semester.objects.create(grade=1.0, student=sone, student_class=cone)
        Semester.objects.create(grade=1.1, student=sone, student_class=ctwo)
        Semester.objects.create(grade=1.2, student=sone, student_class=cthree)

        Semester.objects.create(grade=2.2, student=stwo, student_class=cone)
        Semester.objects.create(grade=2.3, student=stwo, student_class=cthree)

    def test_student_name_property(self):
        """ Test to ensure method property first name properly adds first_name and last_name"""
        sone = Student.objects.filter(email="email@example.com").first()
        self.assertEquals(sone.name, "First Name Last Name")

    def test_student_average_gpa(self):
        """ Test to ensure method property average_gpa computers average gpa"""
        sone = Student.objects.filter(email="email@example.com").first()
        self.assertEquals(sone.average_gpa, (1.0 + 1.1 + 1.2) / 3)

    def test_student_my_classes(self):
        """ Test to ensure method my_classes returns a list of students classes"""
        sone = Student.objects.filter(email="email@example.com").first()
        self.assertEquals(sone.my_classes(), [{'grade': 1.0, 'id': 1}, {'grade': 1.1, 'id': 2}, {'grade': 1.2, 'id': 3}])

    def test_student_to_dict(self):
        """ Test to ensure method to_dict returns dictionary representaton of Student"""
        sone = Student.objects.filter(email="email@example.com").first()
        self.assertEquals(sone.to_dict(), {'first': u'First Name',
                                           'last': u'Last Name',
                                           'studentClasses': [{'grade': 1.0, 'id': 1},
                                                              {'grade': 1.1, 'id': 2},
                                                              {'grade': 1.2, 'id': 3}],
                                           'email': u'email@example.com'})

    def test_student_class_to_dict(self):
        """ Test to ensure method to_dict returns dictionary representaton of StudentClass"""
        cone = StudentClass.objects.filter(description="Math 101").first()
        self.assertEquals(cone.to_dict(), {'1': u'Math 101'})

    def test_semester_to_dict(self):
        """ Test to ensure method to_dict returns dictionary representaton of SemesterClass"""
        astudent = Student.objects.filter(email="email@example.com").first()
        asemester = Semester.objects.filter(grade=1.0, student=astudent).first()
        self.assertEquals(asemester.to_dict(), {'grade': 1.0, 'id': 1})

    def test_student_get_request_all(self):
        """Asserts the students view with no parms returns full payload
        """
        request_factory = RequestFactory()
        request = request_factory.get('/students/')

        response = json.loads(StudentView.as_view()(request)._container[0])

        self.assertEquals(len(response["students"]), 2)
        self.assertEquals(len(response["classes"]), 3)

    def test_student_filterview(self):
        """Asserts the students view with no parms returns full payload
        """
        request_factory = RequestFactory()
        request = request_factory.get('/students/?first_name=First&average_gpa=1.0999999999999999',
                                      data={'first_name': 'First', 'average_gpa': 1.0999999999999999})

        response = json.loads(StudentView.as_view()(request)._container[0])

        self.assertEquals(len(response["students"]), 1)
        self.assertEquals(response["students"][0]["first"], "First Name")
