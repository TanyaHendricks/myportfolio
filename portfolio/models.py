from typing import Any
from django.db import models
import uuid

from django.db.models.fields import AutoField

# Create your models here.


class Interest(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

class Website(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    url = models.URLField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

class Institution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=1000, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True, default="Default.png")
    website_id = models.ForeignKey(Website, on_delete=models.RESTRICT, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name 

class DocumentType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name

class Experience(models.Model):
    EXPERIENCE_TYPE = (
        ('Education', 'Learning Experience'),
        ('Employement', 'Employment Experience'),
        ('Project', 'Project Experience'),
    )
    type = models.CharField(max_length=100, null=False, blank=False, default='', choices=EXPERIENCE_TYPE)
    title = models.CharField(max_length=100, null=False, blank=False)
    institution_id = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    commenced = models.DateField(null=False, blank=False)
    completed = models.DateField(null=False, blank=False)
    description = models.TextField(max_length=1000)
    tags = models.ManyToManyField('Tag', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

class Document(models.Model):    
    document_type = models.ForeignKey(DocumentType, on_delete=models.RESTRICT, default='')
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    issued_id = models.DateField(null=False, blank=False)
    issuer_id = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    experience_id = models.ForeignKey(Experience, on_delete=models.RESTRICT, null=False, blank=False, default='')
    image = models.ImageField(null=False, blank=False, default="Default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title  

class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=10, null=False, blank=False, unique=True)
    description = description = models.TextField(max_length=300, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    url = models.URLField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name