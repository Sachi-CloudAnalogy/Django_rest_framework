# Model View Set
from .models import Student
from .model_serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

#can perform all the crud operations
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]

    # permission_classes = [IsAuthenticated]   #only registeed user can access
    # permission_classes = [AllowAny]          #anyone can access
    # permission_classes = [IsAdminUser]       #members whose is_staff = true, only they can access
