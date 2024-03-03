from PyPDF3 import PdfFileMerger

merger = PdfFileMerger()

# Assuming that the PDF files are in the same directory as your script
pdf_files = ["Cover Page Group Assignment.pdf", "Impact of Climate Change on Sustainable Development Goal 14.pdf"]

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
