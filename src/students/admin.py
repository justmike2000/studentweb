from django.contrib import admin

from students.models import (Student, StudentClass, Semester)


class StudentAdmin(admin.ModelAdmin):
    pass


class StudentClassAdmin(admin.ModelAdmin):
    pass


class SemesterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(Semester, SemesterAdmin)
