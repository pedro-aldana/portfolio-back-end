from django.db import models
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

def project_thumbnail_directory(instance,filename):
    return 'project/{0}/{1}'.format(instance,filename)


class Project(models.Model):
    
    title = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(max_length=255,unique=True, default=uuid.uuid4)
    description =   models.TextField(max_length=255,blank=True, null=True)
    content =       RichTextField(blank=True, null=True)
    language = models.CharField(max_length=255,blank=True,null=True)
    url = models.CharField(max_length=600,blank=True,null=True)
    thumbnail =     models.ImageField(upload_to=project_thumbnail_directory,max_length=500,blank=True, null=True)
    
    
    
    
    
    def __str__(self) -> str:
        return self.title
    
    
    