import pdfquery
import pandas as pd
from google import genai
import markdown

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PDFQuery."""
    pdf = pdfquery.PDFQuery(pdf_path)
    pdf.load()
    
    # Convert PDF to XML (optional, for debugging)
    pdf.tree.write('output.xml', pretty_print=True)

    # Extract all text elements
    text_elements = pdf.pq('LTTextLineHorizontal')
    text = [t.text for t in text_elements]
    
    return "\n".join(text)


def generate_summary_prompt(extracted_text):
    prompt = (
        "Please summarize the following content in clear and simple English. "
        "Ensure that the main ideas are easy to understand. Additionally, "
        "feel free to include any relevant information that enhances the summary or provides more context. "
        f"Here is the text:\n\n{extracted_text}\n"
    )
    return prompt





def summarize_text(text, api_key):
    """Summarize the extracted text using the Gemini API with a custom prompt."""
    client = genai.Client(api_key='<gemini api>')
       
    # Generate the prompt using the extracted text
    prompt = generate_summary_prompt(text)
       
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
       
    return markdown.markdown(response.text)
