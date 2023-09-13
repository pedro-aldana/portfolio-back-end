from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListProjects.as_view() ),
    path('detail/<slug>', ProjectDetailView.as_view()),
    
    path('enviar-correo', ContactFormAPI.as_view()),
]