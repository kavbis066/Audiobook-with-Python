# this program converts a PDF to audiobook

#Import libraries
import pyttsx3
import pdfplumber
import PyPDF2

#Get the file and the location
file = 'The Billionaires Price by Corsino Ansela.pdf'

#Create a PDF file object
pdfFileObj = open(file, 'rb')

#Create the PDF file reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the number of pages
pages = pdfReader.numPages

#Create a PDF plumber object and loop through the number of pages in PDF file
with pdfplumber.open(file) as pdf:
    #Loop through the pages
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()