import pdftotext
import json
with open("/home/kamalhem/Downloads/Mahadiscom-master/0050095766.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)


print(len(pdf))
page = pdf[0]

print(page)

print('Bill date', page[105:115])
print('Due date',page[133:143])

print('Usage (SCM)',page[713:719])

print('Bill Amount', page[1894:1900])
