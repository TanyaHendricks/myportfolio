from django.urls import path
from . import views

urlpatterns = [    
    path('', views.portfolio, name="portfolio" ),
    path('document/<str:pk>', views.viewDocument, name="document" ),
]

