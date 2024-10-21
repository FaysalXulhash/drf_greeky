from django.contrib import admin
from django.urls import path, include
#from api.views import StudentApi, studentDetailApi
from api.views import Studentviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', Studentviewset, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include(router.urls),),
    #path('student/', StudentApi.as_view(), name='student'),
    #path('student/<int:pk>/', studentDetailApi.as_view(), name='student-details'),
]
   