from typing import List
from django.shortcuts import render
from .models import Interest
from .models import Document
from .models import DocumentType
from .models import Reference
from .models import Experience
from .models import Institution
from .models import Video

def portfolio(request):
    interests = Interest.objects.all()
    testimonialDocumentType = DocumentType.objects.get(name="Testimonial")
    testimonials = Document.objects.filter(
        document_type=testimonialDocumentType)
    references = Reference.objects.all()
    experiences = Experience.objects.all().order_by('completed')    
    institutions = Institution.objects.all()   
    context = {'interests': interests, 
               'testimonials': testimonials, 'references': references,
               'experiences': experiences, 'institutions' : institutions}
    return render(request, 'portfolio/portfolio.html', context)


def viewDocument(request, pk):
    document = Document.objects.get(id=pk)
    print(document)
    return render(request, 'portfolio/document.html', {'document': document})


def viewVideo(request, pk):
    video = Video.objects.get(id=pk)
    print(video)
    return render(request, 'portfolio/video.html', {'video': video})