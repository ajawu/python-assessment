from django.contrib import admin
from django.urls import path, include


BASE_URL = 'v1/api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(f'{BASE_URL}/asssessment/', include('assessment.urls'))
]
