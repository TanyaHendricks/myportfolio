from django.db import models

# Create your models here.

class Interest(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    def _str_(self):
        return self.title

class Website(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = models.ImageField(null=False, blank=False)
    url = models.URLField(null=False, blank=False)
    def _str_(self):
        return self.title

class Institution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True)
    website = models.ForeignKey(Website, on_delete=models.RESTRICT, null=True, blank=True)
    def _str_(self):
        return self.name 

class DocumentType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=False, blank=False)
    def _str_(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    institution = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    commenced = models.DateField()
    completed = models.DateField()
    description = models.TextField(max_length=1000, null=False, blank=False)
    def _str_(self):
        return self.title

class Document(models.Model):    
    document_type = models.ForeignKey(DocumentType, on_delete=models.RESTRICT)
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    issued = models.DateField()
    issuer = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    experience = models.ForeignKey(Experience, on_delete=models.RESTRICT, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    def _str_(self):
        return self.title  



