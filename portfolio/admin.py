from django.contrib import admin
from .models import Interest
from .models import Website
from .models import Institution
from .models import DocumentType
from .models import Experience
from .models import Document
from .models import Tag

# Register your models here.

admin.site.register(Interest)
admin.site.register(Website)
admin.site.register(Institution)
admin.site.register(DocumentType)
admin.site.register(Experience)
admin.site.register(Document)
admin.site.register(Tag)
