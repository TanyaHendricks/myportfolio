from django.shortcuts import render


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def viewDocument(request, pk):
    return render(request, 'portfolio/document.html')