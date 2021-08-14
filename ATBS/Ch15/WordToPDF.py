# thsi script runs on windows only and you must have Word installed.
import win32com.client
import docx

wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'

doc -docx.Document()
# code to create a word document

doc.save(wordFilename)

wdFormatPDF = 17 # words numeric code for pdfs

wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()