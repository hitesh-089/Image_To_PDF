import base64

with open('E:\Hitesh Docs\Web Devlopment\CSV_Converter\pdf_file\Hitesh.pdf','rb') as imageFile:
        val = base64.b64encode(imageFile.read())
print(val)