import pyttsx3
import PyPDF2

book_name = open('harrypotter.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(book_name)
pages = pdf_reader.numPages

play = pyttsx3.init()
print('playing....')

for num in range(0,pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    play.say(text)
    play.runAndWait()