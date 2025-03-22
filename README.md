# PDF Summarizer

## Table of Contents
- [Project Overview](#project-overview)
- [Key Technologies Used](#key-technologies-used)
- [System Design Diagram](#system-design-diagram)
- [Features and Functionality](#features-and-functionality)
- [File Structure](#file-structure)
- [Folder Description](#folder-description)
- [Future Enhancements](#future-enhancements)

## Project Overview
PDF Summarizer is a Django-based web application that allows users to upload PDF files, extract text content, and generate AI-powered summaries. The application uses Google's Gemini AI model to process the extracted text and provide concise, readable summaries. This tool is designed to help users quickly understand the essential content of PDF documents without having to read through the entire text.

## Key Technologies Used
### Backend Framework:
- Django 5.1.7
- Python 3
- PostgreSQL database

### Frontend:
- HTML/CSS
- Bootstrap 5.3.3
- Django templates

### PDF Processing:
- PDFQuery for text extraction
- XML parsing

### AI Integration:
- Google Gemini AI (gemini-2.0-flash model)
- Markdown for formatting AI responses

## System Design Diagram
![System Design Diagram](<./System Design.png>)


## Features and Functionality
1. **PDF Upload**
    - User-friendly interface for uploading PDF files
    - Validation for file formats

2. **Text Extraction**
    - Automated extraction of text content from uploaded PDFs
    - XML conversion for structured data representation

3. **Summary Generation**
    - Integration with Google's Gemini AI for summarization
    - Custom prompt engineering for better summary quality
    - Markdown formatting of AI responses for readability

4. **User Interface**
    - Clean Bootstrap-based design
    - Responsive layout
    - Navigation between upload and summary views

## File Structure
```
pdf_project/
│
├── manage.py               # Django management script
├── output.xml              # Output from PDF extraction
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── pdf_logic/              # Main application
│   ├── __init__.py
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── pdf_handler.py      # PDF processing logic
│   ├── tests.py            # Unit tests
│   ├── urls.py             # App URL definitions
│   ├── views.py            # View functions
│   ├── migrations/         # Database migrations
│   └── __pycache__/        # Python cache files
│
├── pdf_project/            # Project settings
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL patterns
│   ├── wsgi.py             # WSGI configuration
│   ├── __pycache__/        # Python cache files
│   └── static/             # Static files
│
├── templates/              # HTML templates
│   ├── layout.html         # Base template
│   ├── summary_new.html    # Summary display template
│   └── upload.html         # File upload template
│
└── uploads/                # Uploaded PDF files
     ├── Akash_Capgemini.pdf
     ├── Akash_Kumar_FIDELITY.pdf
     ├── PythonTask.pdf
     └── Sale_Deed.pdf
```

## Folder Description
- **pdf_logic/**: Core application with models, views, and business logic
- **pdf_handler.py**: Contains the PDF text extraction and AI summarization functionality
- **migrations/**: Database migration files for maintaining database schema
- **pdf_project/**: Project configuration files including settings, URL patterns
- **static/**: Contains CSS, JavaScript, and other static files
- **templates/**: HTML templates using Django's template language
  - **layout.html**: Base template with common layout elements
  - **upload.html**: Template for the PDF upload page
  - **summary_new.html**: Template for displaying extracted text and summaries
- **uploads/**: Directory for storing uploaded PDF files

## Future Enhancements
1. **User Authentication and Management**
    - User registration and login
    - Personal dashboard for managing uploaded PDFs

2. **Enhanced PDF Processing**
    - Image extraction and analysis using OCR (Optical Character Recognition)
    - Table detection and structured data extraction
    - Support for multiple file formats

3. **Advanced AI Features**
    - Multiple summary styles (brief, detailed, bullet points)
    - Entity extraction and highlighting
    - Multiple language support

4. **Performance Improvements**
    - Asynchronous processing for large PDFs
    - Caching strategies using Redis for faster response times
    - Background processing using Celery

5. **UI/UX Enhancements**
    - PDF preview functionality
    - Interactive summary editing
    - Advanced search capabilities

6. **Frontend Technology**
    - Use React instead of HTML for a more dynamic user interface

7. **Database and Storage**
    - Use AWS RDS for database storage
    - Implement Redis for caching
 ## Demo Video
 [Watch the application demo](https://drive.google.com/file/d/170HSxfNAkLZMyGoA9bWpYAZB8-YtYkoK/view?usp=sharing)