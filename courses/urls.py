from django.urls import path
from .views import *

app_name = "course"

urlpatterns = [
    path('', CourseListView.as_view(), name="course"),
    path('create/', CourseCreateView.as_view()),
    path('<int:id>/', CourseDetailView.as_view()),
    path('<int:id>/edit/', CourseUpdateView.as_view()),
    path('<int:id>/delete/', CourseDeleteView.as_view()),
]
