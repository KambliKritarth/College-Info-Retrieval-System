from django.contrib import admin
from django.urls import path, include 
from clginfoblog import views


admin.site.site_header = "CIRS"
admin.site.site_title = "CIRS's Dashboard"
admin.site.index_title = "Welcome to the dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clginfoblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

