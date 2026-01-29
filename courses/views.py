from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses
from enrollments.models import Enrollments
from django.core.exceptions import ValidationError


class CourseListView(View):
    def get(self, request):
        courses = Courses.objects.all()
        return render(request, "courses/list.html", {"courses": courses})



class CourseCreateView(View):
    def get(self, request):
        return render(request, "courses/create.html")

    def post(self, request):
        Courses.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description'),
            duration_weeks=request.POST['duration_weeks']
        )
        return redirect("course:course")



class CourseDetailView(View):
    def get(self, request, id):
        course = get_object_or_404(Courses, id=id)
        students = Enrollments.objects.filter(course=course)
        return render(request, "courses/detail.html", {
            "course": course,
            "students": students
        })



class CourseUpdateView(View):
    def get(self, request, id):
        course = get_object_or_404(Courses, id=id)
        return render(request, "courses/edit.html", {"course": course})

    def post(self, request, id):
        course = get_object_or_404(Courses, id=id)
        course.title = request.POST['title']
        course.description = request.POST.get('description')
        course.duration_weeks = request.POST['duration_weeks']
        course.save()
        return redirect("/courses/")



class CourseDeleteView(View):
    def post(self, request, id):
        course = get_object_or_404(Courses, id=id)
        try:
            course.delete()
        except ValidationError as e:
            return render(request, "/courses/")
        return redirect("/courses/")
