from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFUpload
from .pdf_handler import extract_text_from_pdf, summarize_text

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_upload = PDFUpload(file=request.FILES['pdf_file'])
            pdf_upload.save()
            # Extract text from the PDF
            extracted_text = extract_text_from_pdf(pdf_upload.file.path)
            pdf_upload.extracted_text = extracted_text
            pdf_upload.save()
            return redirect('summary', pdf_upload.id)
    else:
        form = PDFUploadForm()
    return render(request, 'upload.html', {'form': form})

def summary(request, pdf_id):
    pdf_upload = PDFUpload.objects.get(id=pdf_id)
    if request.method == 'POST':
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        summary_text = summarize_text(pdf_upload.extracted_text, api_key)
        return render(request, 'summary_new.html', {'pdf_upload': pdf_upload, 'summary': summary_text})
    
    return render(request, 'summary_new.html', {'pdf_upload': pdf_upload})

def home(request):
    return redirect('upload_pdf') 