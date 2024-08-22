from django.contrib import admin
from django.urls import path
from drf_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>', views.student_detail),
    path('student/', views.student_list),
    path('student_create/', views.student_create), 
    path('studentapi/', views.student_api),
]
