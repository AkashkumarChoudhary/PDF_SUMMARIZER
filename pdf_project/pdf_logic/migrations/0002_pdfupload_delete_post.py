# Generated by Django 5.1.7 on 2025-03-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('extracted_text', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
