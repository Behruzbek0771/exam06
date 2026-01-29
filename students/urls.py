from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListView.as_view()),
    path('create/', StudentCreateView.as_view()),
    path('<int:id>/', StudentDetailView.as_view()),
    path('<int:id>/delete/', StudentDeleteView.as_view()),
]
