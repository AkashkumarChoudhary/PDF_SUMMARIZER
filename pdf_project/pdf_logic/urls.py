from django.urls import path
from .views import upload_pdf, summary

urlpatterns = [
    path('', upload_pdf, name='upload_pdf'),
    path('summary/<int:pdf_id>/', summary, name='summary'),
]