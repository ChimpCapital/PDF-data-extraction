import pyPDF2

def main():
    pdfFile = "PDF/Q1.pdf"
    pdfRead = pyPDF2.pdfReader (pdfFile)
    page = pdfRead.getPage(5)
    pageContent =page.extractText()
    print (pageContent)

    if __name_ == "__main__":
        main()
