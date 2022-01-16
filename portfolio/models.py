from django.db import models
import uuid
from embed_video.fields import EmbedVideoField

# Create your models here.

class Interest(models.Model):
    title = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Website(models.Model):
    title = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    url = models.URLField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Institution(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    description = models.TextField(max_length=1000, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True, default="Default.png")
    website_id = models.ForeignKey(
        Website, on_delete=models.RESTRICT, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Experience(models.Model):
    EXPERIENCE_TYPE = (
        ('Qualification', 'Qualification Experience'),
        ('Employment', 'Employment Experience'),
        ('Project', 'Project Experience'),
        ('Workshop', 'Workshop Experience'),
        ('Short Course', 'Short Course Experience'),
    )
    type = models.CharField(max_length=100, null=False,
                            blank=False, default='', choices=EXPERIENCE_TYPE)
    title = models.CharField(max_length=100, null=False, blank=False)
    institution_id = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    commenced = models.DateTimeField(null=False, blank=False)
    completed = models.DateTimeField(null=False, blank=False)
    description = models.TextField(max_length=2100)
    tags = models.ManyToManyField('Tag', blank=True)
    documents = models.ManyToManyField('Document')    
    videos = models.ManyToManyField('Video', blank=True)    
    websites = models.ManyToManyField('Website', blank=True)  
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.title


class Document(models.Model):
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.RESTRICT, default='')
    title = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    issued_id = models.DateTimeField(null=False, blank=False)
    issuer_id = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
                                

class Video(models.Model):
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.RESTRICT, default='')
    title = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    url = models.URLField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Reference(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=10, null=False,
                             blank=False, unique=True)
    description = description = models.TextField(
        max_length=300, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, default="Default.png")
    url = models.URLField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
