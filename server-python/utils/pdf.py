from pypdf import PdfReader

def process_file(file):
   text = ""

   file = PdfReader(file)

   for page in file.pages:
      text += page.extract_text()
   return text