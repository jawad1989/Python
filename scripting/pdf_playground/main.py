'''https://pythonhosted.org/PyPDF2/index.html
read pdf
rotate pdf
write new pdf
get page
count pages''' 

import PyPDF2

with open('pdfs/tcs.pdf','rb') as mypdf:
    reader = PyPDF2.PdfFileReader(mypdf)
    print(reader.numPages)
    print(reader.getPage(3))
    
    page = reader.getPage(1)
    page.rotateClockwise(180)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdfs/tcs-tilt.pdf','wb') as new_file:
        writer.write(new_file)
