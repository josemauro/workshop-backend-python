from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class ProfessorAPIView(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
