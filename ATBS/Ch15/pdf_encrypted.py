import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

print(pdfReader.isEncrypted)

pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)