import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('oop.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
page = pdfReader.getPage(2)
text = page.extractText()

speaker.say(text)
speaker.runAndWait()