"""python merge_pdf jawad.pdf bill.pdf """

import PyPDF2
import sys

input = sys.argv[1:]

def merge_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        conc = "pdfs/"+pdf
        merger.append(conc)
    merger.write("pdfs/merged2.pdf")

merge_pdf(input)
