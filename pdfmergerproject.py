from PyPDF2 import PdfReader, PdfWriter

pdf_writer = PdfWriter()
#adding pdf to be merged
for pdf_file in [r"C:\Users\deepi\Documents\mpdf.pdf", r"C:\Users\deepi\Downloads\Fuel.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        pdf_writer.add_page(page)

#saving merged pdf
with open('merged.pdf', 'wb') as merged_file:
    pdf_writer.write(merged_file)