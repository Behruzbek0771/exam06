from django.views import View
from django.shortcuts import render, redirect
from .models import Enrollments
from students.models import Students
from courses.models import Courses
from django.db import IntegrityError

class EnrollmentListView(View):
    def get(self, request):
        data = Enrollments.objects.all()
        return render(request, "enrollments/list.html", {"data": data})


class EnrollmentCreateView(View):
    def get(self, request):
        return render(request, "enrollments/create.html", {
            "students": Students.objects.all(),
            "courses": Courses.objects.all()
        })

    def post(self, request):
        try:
            Enrollments.objects.create(
                student_id=request.POST['student'],
                course_id=request.POST['course']
            )
            return redirect("/enrollments/")
        except IntegrityError:
            return render(request, "error.html", {
                "msg": "Student allaqachon yozilgan!"
            })
