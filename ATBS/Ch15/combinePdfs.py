#! python3
# combinedPdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.
import PyPDF2, os
# Get all the PDF filenames

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# loop through all the pdf files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


# save the resulting pdf to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()