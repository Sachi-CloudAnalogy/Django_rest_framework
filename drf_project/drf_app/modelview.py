# Model View Set
from .models import Student
from .model_serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from drf_app.throttling import JackRateThrottle
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter 
from .pagination import MyPagination

#can perform all the crud operations
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [BasicAuthentication]
    
    # permission_classes = [IsAuthenticated]   #only registered user can access
    # permission_classes = [AllowAny]          #anyone can access
    # permission_classes = [IsAdminUser]       #members whose is_staff = true, only they can access

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]

class StudentList(ListAPIView):
    # queryset = Student.objects.filter(city="Delhi")
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_queryset(self):      # used to filter 
    #     user = self.request.user
    #     print(user)
    #     return Student.objects.filter(roll_no=104)
    
    filter_backends = [DjangoFilterBackend]     #for per view setting, different filter for every view
    filterset_fields = ['name', 'city']     #fields on which you want to filter

#http://127.0.0.1:8000/studentlist/?name=Kajal&city=Delhi   ---in url


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['name','city']      #can search either with name or with city
    search_fields = ['^name']              #starts with search
# http://127.0.0.1:8000/student_list/?search=Ranchi       ---in url

class StudentLV(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]    # to filter entries in some order
    ordering_fields = ['name']            #optional
# http://127.0.0.1:8000/student_filter/?ordering=name    

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination
