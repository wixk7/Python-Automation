import pyttsx3
import pdfplumber
from PyPDF2 import PdfReader

file = 'test.pdf'
all_text = []

try:
    s = pyttsx3.init()
    pdf_reader = PdfReader(file)
    pages = len(pdf_reader.pages)

    with pdfplumber.open(file) as pdf:
        for i in range(pages):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                all_text.append(text)
                print(f"\n{text}\n")
                s.say(text)
                audio_file_name = f'audio_page_{i + 1}.mp3'
                s.save_to_file(text, audio_file_name)

    s.runAndWait()

except FileNotFoundError:
    print('File not found. Please check the file path and name.')
except Exception as e:
    print(f'An error occurred: {str(e)}')

print('Audio files saved successfully.')
