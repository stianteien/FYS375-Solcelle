# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:16:02 2021

@author: Stian
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
input_pdf = PdfFileReader("Databehandling.pdf")
output = PdfFileWriter()
output.addPage(input_pdf.getPage(0))
with open("FYS375 LAB3 Databehandling.pdf", "wb") as output_stream:
    output.write(output_stream)