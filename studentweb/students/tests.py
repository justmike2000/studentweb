from django.test import TestCase

from models import (Student, StudentClass, Semester)

class StudentTestCase(TestCase):

    def setUp(self):
        s1 = Student.objects.create(first_name="First Name",
                                   last_name="Last Name",
                                   email="email@example.com")
        s2 = Student.objects.create(first_name="Bobby",
                                   last_name="Smith",
                                   email="bobbysmith@example.com")
        
        c1 = StudentClass.objects.create(description="Math 101")
        c2 = StudentClass.objects.create(description="Math 201")
        c3 = StudentClass.objects.create(description="English 101")
  
        Semester.objects.create(grade=1.0, student=s1, student_class=c1)
        Semester.objects.create(grade=1.1, student=s1, student_class=c2)
        Semester.objects.create(grade=1.2, student=s1, student_class=c3)

        Semester.objects.create(grade=2.2, student=s2, student_class=c1)
        Semester.objects.create(grade=2.3, student=s2, student_class=c3)

    def test_student_name_property(self):
        """Test to ensure method property first name properly adds first_name and last_name
        """    
        s = Student.objects.filter(email="email@example.com").first()
       
        self.assertEquals(s.name, "First Name Last Name")

    def test_student_average_gpa(self):
        """Test to ensure method property average_gpa computers average gpa
        """    
        s = Student.objects.filter(email="email@example.com").first()
       
        self.assertEquals(s.average_gpa, 1.6)

    def test_student_my_classes(self):
        """Test to ensure method my_classes returns a list of students classes
        """    
        s = Student.objects.filter(email="email@example.com").first()

        self.assertEquals(s.my_classes(), [{'grade': 1.0, 'id': 1}, {'grade': 2.2, 'id': 1}])

    def test_student_to_dict(self):
        """Test to ensure method to_dict returns dictionary representaton of Student
        """    
        s = Student.objects.filter(email="email@example.com").first()

        self.assertEquals(s.to_dict(), {'first': u'First Name',
                                        'last': u'Last Name',
                                        'studentClasses': [{'grade': 1.0, 'id': 1},
                                                           {'grade': 2.2, 'id': 1}],
                                        'email': u'email@example.com'})

    def test_student_class_to_dict(self):
        """Test to ensure method to_dict returns dictionary representaton of StudentClass
        """    
        c1 = StudentClass.objects.filter(description="Math 101").first()

        self.assertEquals(c1.to_dict(), {'1': u'Math 101'})

    def test_semester_to_dict(self):
        """Test to ensure method to_dict returns dictionary representaton of SemesterClass
        """    
        s = Student.objects.filter(email="email@example.com").first()
        s1 = Semester.objects.filter(grade=1.0, student=s).first()

        self.assertEquals(s1.to_dict(), {'grade': 1.0, 'id': 1})
