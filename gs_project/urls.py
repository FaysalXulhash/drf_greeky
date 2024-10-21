from django.contrib import admin
from django.urls import path, include
from api.views import StudentApi, studentDetailApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('student/', StudentApi.as_view(), name='student'),
    path('student/<int:pk>/', studentDetailApi.as_view(), name='student-details'),
]
