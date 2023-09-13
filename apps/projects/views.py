from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Project
from .serializers import ProjectSerializer,ProjectListSerializer
from .pagination import SmallSetPagination,MediumSetPagination,LargeSetPagination
from django.http import JsonResponse
import smtplib
from email.mime.text import MIMEText
from django.conf import settings


# Enviar Email

# def send_email(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # Configurar el servidor SMTP de Gmail
#         smtp_server = settings.EMAIL_HOST
#         smtp_port = settings.EMAIL_PORT
#         smtp_username = settings.EMAIL_HOST_USER
#         smtp_password = settings.EMAIL_HOST_PASSWORD
        
#         # Crear el mensaje de correo
#         subject = 'Formulario de contacto'
#         body = f'Nombre: {name}\nApellido: {last_name}\nCorreo electronico: {email}\nMensaje: {message}'
#         msg = MIMEText(body)
#         msg['Subject'] = subject
#         msg['From'] = smtp_username
#         msg['To'] = 'pedroaldana987@gmail.com'
        
#         try:
#             # Conectar al servidor SMTP y envia el correo
#             server = smtplib.SMTP(smtp_server, smtp_port)
#             server.starttls()
#             server.login(smtp_username, 'pedroaldana987@gmail.com', msg.as_string())
#             server.quit()
#             return JsonResponse({'message': 'Correo enviado con exito'})
        
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
                


# Create your views here.



class ListProjects(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self,request,format=None):
        
        if Project.objects.all().exists():
            
            project = Project.objects.all()
            
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(project,request)
            
            serializer = ProjectListSerializer(results, many=True)
            
            return paginator.get_paginated_response({'project': serializer.data})
        else:
            return Response({'error': 'No se encontraron proyectos'}, status=status.HTTP_404_NOT_FOUND)
            
            

class ProjectDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self,request,slug,format=None):
        if Project.objects.filter(slug=slug).exists():
             
            project = Project.objects.get(slug=slug)   
            
            serializer = ProjectSerializer(project)
            
            return Response({'project': serializer.data})
        else:
            return Response({'error','No se encontro el proyecto'}, status=status.HTTP_404_NOT_FOUND)                        
        
        
        
class ContactFormAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        if request.method == 'POST':
            name = request.data.get('name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            message = request.data.get('message')
            
            # Configurar el servidor SMTP de Gmail
            smtp_server = settings.EMAIL_HOST
            smtp_port = settings.EMAIL_PORT
            smtp_username = settings.EMAIL_HOST_USER
            smtp_password = settings.EMAIL_HOST_PASSWORD
            
            # Crear el mensaje de correo
            subject = 'Formulario de contacto'
            body = f'Nombre: {name}\nApellido: {last_name}\nCorreo electronico: {email}\nMensaje: {message}'
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = 'pedroaldana987@gmail.com'
            
            try:
                # Conectar al servidor SMTP y envia el correo
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(smtp_username,smtp_password)
                server.sendmail(smtp_username, 'pedroaldana987@gmail.com', msg.as_string())
                server.quit()
                return Response({'message': 'Correo enviado con exito'}, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            