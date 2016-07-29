from django.db import models


class Student(models.Model):
    """ Student Django Model
        - Represents a student (Sally Salt)
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        """ Returns a unicode representation of this class"""
        return "%d %s %s" % (self.id, self.name, self.email,)

    def my_classes(self):
        """ Returns a list of classes and grades for a student"""
        classes = []
        for semester in Semester.objects.filter(student_class=self.id).all():
             classes.append(semester.to_dict())
        return classes

    def to_dict(self):
        """ Returns a dictionary representation of this class"""
        student_dict = {}
        student_dict["studentClasses"] = self.my_classes()
        student_dict["email"] = self.email
        split_name = self.name.split(" ")
        student_dict["first"] = split_name[0]
        try:
            student_dict["last"] = split_name[-1]
        except IndexError:
            pass

        return student_dict


class StudentClass(models.Model):
    """ StudentClass Django Model
        - Identifies a student class (i.e. Math 101) 
    """
    description = models.CharField(max_length=255)

    def to_dict(self):
        """ Returns a dictionary representation of this class"""
        return {"%d" % (self.id,): self.description}

    def __unicode__(self):
        """ Returns a unicode representation of this class"""
        return "%d %s" % (self.id, self.description,)


class Semester(models.Model):
    """ Semester Django Model
        - Represents a relation between student and class (i.e. Sally Salt with a 2.0 grade) 
    """
    student = models.ForeignKey(Student)
    student_class = models.ForeignKey(StudentClass)
    grade = models.FloatField()

    class Meta:
        """ Meta sublass to specify composite unique fields"""
        unique_together = (('student', 'student_class'),)

    def to_dict(self):
        """ Returns a dictionary representation of this class"""
        return {"id": self.student_class.id, "grade": self.grade}

    def __unicode__(self): 
        """ Returns a unicode representation of this class"""
        return "%d %s %s %d" % (self.id, self.student.name, self.student_class.description, self.grade)
