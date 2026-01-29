from django.urls import path
from .views import *

urlpatterns = [
    path('', EnrollmentListView.as_view()),
    path('create/', EnrollmentCreateView.as_view()),
]
