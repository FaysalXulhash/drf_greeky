
from django.contrib import admin
from django.urls import path, include
from api.views import index, details 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', index, name='index'),
    path('<int:pk>/', details, name='details'),
]
