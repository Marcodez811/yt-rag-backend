from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


class CourseAPI(APIView):
    """
    List all courses of the user, create a new course for the user.
    """

    def get(self, request):
        user = request.user
        courses = Course.objects.filter(owner=user)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
