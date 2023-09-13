from django.db import models
from django.db.models.query import QuerySet
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

def project_thumbnail_directory(instance,filename):
    return 'project/{0}/{1}'.format(instance,filename)


class Project(models.Model):
    
    class PostObject(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='title')
        
        
    
    title = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(max_length=255,unique=True, default=uuid.uuid4)
    description =   models.TextField(max_length=255,blank=True, null=True)
    content =       RichTextField(blank=True, null=True)
    language = models.CharField(max_length=255,blank=True,null=True)
    url = models.CharField(max_length=600,blank=True,null=True)
    thumbnail =     models.ImageField(upload_to=project_thumbnail_directory,max_length=500,blank=True, null=True)
    
    class Meta:
        ordering = ['title']
    
    
    
    
    
    def __str__(self) -> str:
        return self.title
    
    
    