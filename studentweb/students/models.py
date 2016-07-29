from django.db import models


class Student(models.Model):
    """
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return "%d %s %s" % (self.id, self.name, self.email,)

    def my_classes(self):
        """
        """
        classes = []
        for semester in Semester.objects.filter(student_class=self.id).all():
             classes.append(semester.to_dict())
        return classes

    def to_dict(self):
        """
        """
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
    """
    """
    description = models.CharField(max_length=255)

    def to_dict(self):
        """
        """
        return {"%d" % (self.id,): self.description}

    def __unicode__(self):
        return "%d %s" % (self.id, self.description,)


class Semester(models.Model):
    """
    """
    student = models.ForeignKey(Student)
    student_class = models.ForeignKey(StudentClass)
    grade = models.FloatField()

    class Meta:
        unique_together = (('student', 'student_class'),)

    def to_dict(self):
        """
        """
        return {"id": self.student_class.id, "grade": self.grade}

    def __unicode__(self):
        return "%d %s %s %d" % (self.id, self.student.name, self.student_class.description, self.grade)
