from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from enrollments.models import Enrollments

class StudentListView(View):
    def get(self, request):
        students = Students.objects.all()

        min_age = request.GET.get("min_age")
        search = request.GET.get("search")

        if min_age:
            students = students.filter(age__gte=min_age)

        if search:
            students = students.filter(full_name__icontains=search)

        return render(request, "students/list.html", {"students": students})


class StudentCreateView(View):
    def get(self, request):
        return render(request, "students/create.html")

    def post(self, request):
        Students.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            age=request.POST['age']
        )
        return redirect("/students/")


class StudentDetailView(View):
    def get(self, request, id):
        student = get_object_or_404(Students, id=id)
        enrollments = Enrollments.objects.filter(student=student)

        return render(request, "students/detail.html", {
            "student": student,
            "enrollments": enrollments
        })


class StudentDeleteView(View):
    def post(self, request, id):
        student = get_object_or_404(Students, id=id)
        student.delete()
        return redirect("/students/")
