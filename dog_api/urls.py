
from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/', include('dogs.urls')),
]
