from pdf2docx import Converter

def pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
    print(f'Conversion complete: {pdf_file} to {docx_file}')

pdf_file = 'newsletter.pdf'
docx_file = 'doc_output_text.docx'

pdf_to_docx(pdf_file, docx_file)
