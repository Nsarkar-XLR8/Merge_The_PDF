# PDF Merger
Overview
This simple Python script utilizes the PyPDF3 library to merge multiple PDF files into a single PDF file. The script is particularly useful when you want to consolidate different PDF documents, such as the "Cover Page Group Assignment" and "Impact of Climate Change on Sustainable Development Goal 14" into a unified file.

Requirements
Python 3.x
PyPDF3 library (pip install PyPDF3)
Usage
Ensure that you have Python installed on your system. If not, you can download it from python.org.

Install the PyPDF3 library by running the following command in your terminal or command prompt:

bash
Copy code
pip install PyPDF3
Place the script in the same directory as the PDF files you want to merge.

Open the script in a text editor and update the pdf_files list with the names of the PDF files you want to merge.

python
Copy code
pdf_files = ["Cover Page Group Assignment.pdf", "Impact of Climate Change on Sustainable Development Goal 14.pdf"]
Run the script using the following command:

bash
Copy code
python merge_pdfs.py
The merged PDF file will be created in the same directory with the name "merged-pdf.pdf".

Note
Ensure that the PDF files are in the correct order in the pdf_files list, as the script will merge them in the specified sequence.
If your PDF files are located in a different directory, provide the correct paths in the pdf_files list.
Contributors
[Your Name]
[Your Email]
Feel free to contribute to the project by submitting issues or pull requests.

