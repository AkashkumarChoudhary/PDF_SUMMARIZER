from django.db import models

# Create your models here.
class PDFUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    extracted_text = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name