import pikepdf

with pikepdf.open("PSY 1,2,3.pdf", password="Cyra-PSY 01") as pdf:
    pdf.save("PSY 1,2,3_updated.pdf")