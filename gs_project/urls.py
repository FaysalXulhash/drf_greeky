from django.contrib import admin
from django.urls import path, include
from api.views import student_api, student_details_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('student/', student_api, name='student'),
    path('student/<int:pk>/', student_details_api, name='student-details'),
]
