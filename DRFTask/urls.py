from django.contrib import admin
from django.urls import path, include
from mainbox.views import apiOverview

urlpatterns = [
    path('', apiOverview),
    path('api/v1/', include('mainbox.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
