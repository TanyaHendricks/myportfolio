from django.shortcuts import render
from .models import Interest
from .models import Document
from .models import DocumentType
from .models import Reference

def portfolio(request):
    interests = Interest.objects.all()
    documents = Document.objects.all()
    testimonialDocumentType = DocumentType.objects.get(name="Testimonial")
    testimonials = Document.objects.filter(document_type=testimonialDocumentType)
    references = Reference.objects.all()
    context = {'interests': interests, 'documents': documents, 'testimonials': testimonials, 'references': references}    
    return render(request, 'portfolio/portfolio.html', context)

def viewDocument(request, pk):
    document = Document.objects.get(id=pk)
    return render(request, 'portfolio/document.html', {'document': document})





