from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # vistas de la api
    path('api/v1/', include('apps.projects.urls')),
    
    
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


