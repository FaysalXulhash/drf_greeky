from django.contrib import admin
from django.urls import path, include
#from api.views import StudentApi, studentDetailApi
from api.views import Studentviewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views #for get/create token
from api.auth import CustomAuthToken
router = DefaultRouter()
router.register('student', Studentviewset, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls),),
    #path('api-token/', views.obtain_auth_token)
    #path('api-token/', CustomAuthToken.as_view()), # for custom ObtainAuthToken

    #path('student/', StudentApi.as_view(), name='student'),
    #path('student/<int:pk>/', studentDetailApi.as_view(), name='student-details'),
]
   