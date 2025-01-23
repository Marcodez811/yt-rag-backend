from django.urls import path, include
from .views import CourseAPI

urlpatterns = [
    path('courses', CourseAPI.as_view()),
]
