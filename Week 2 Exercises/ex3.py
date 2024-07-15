import PyPDF2
from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'Sense-and-Sensibility-by-Jane-Austen.pdf'

pdfReader = PyPDF2.PdfReader(filename)

page_number = len(pdfReader.pages)

page_object = pdfReader.pages[0]

page_text = page_object.extract_text()

wordsinjane = dict()

allwords = page_text.split(" ")

for x in allwords:
    if(x.isnumeric()) or (x == "CHAPTER") or (x == "page") or (x == "," or x=="." or x==";" or x=="/" or x== ""):
        continue
    else:
        if(x in wordsinjane):
            wordsinjane[x]+=1
        else:
            wordsinjane[x]=1
    
print(wordsinjane)


