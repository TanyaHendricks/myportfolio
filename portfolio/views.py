from django.shortcuts import render
from .models import Interest
from .models import Document

def portfolio(request):
    interests = Interest.objects.all()
    documents = Document.objects.all()
    context = {'interests': interests, 'documents': documents}    
    return render(request, 'portfolio/portfolio.html', context)

def viewDocument(request, pk):
    document = Document.objects.get(id=pk)
    return render(request, 'portfolio/document.html', {'document': document})