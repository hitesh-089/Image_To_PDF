from PIL import Image
from fpdf import FPDF
import os

source_path='./image_file'
image_list = []
for img in os.listdir(source_path):
    image_list.append(Image.open(os.path.join(source_path,img)))

pdf_name = './pdf_file/output.pdf'

image_list[0].save(pdf_name,"PDF",resolution =100.0 , save_all= True, append_images = image_list[1:])