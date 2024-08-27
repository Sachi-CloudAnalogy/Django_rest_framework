from django.contrib import admin
from django.urls import path, include
from drf_app import views, views_api, modelview
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('student_api', modelview.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>', views.student_detail),
    path('student/', views.student_list),
    path('student_create/', views.student_create), 
    # path('studentapi/', views.student_api),
    path('studentapi/', views.StudentAPI.as_view()),   # for class based view
    path('student_apiview/',views_api.hello_world),
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),     #builtin url (to get login and logout options)
    path('gettoken/', obtain_auth_token)
]
