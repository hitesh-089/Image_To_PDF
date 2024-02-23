from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
from PIL import Image
import base64
from io import BytesIO
import os


app =  Flask(__name__,template_folder = "templates")


CORS(app)
@app.route('/')
def render():
    return render_template("Image_to_pdf.html")


@app.route('/process', methods = ['POST'])
def process():

    path  = 'E:\\Hitesh Docs\\Web Devlopment\\Image_To_PDF'
    os.chdir(path)
    imageFolder  = 'image_file'
    os.makedirs(imageFolder)
    pdfFolder = 'pdf_file'
    os.makedirs(pdfFolder)


    dir_path = '.\image_file'


    #Base64 Data is restored from json form
    data = request.get_json()
    store = data['value']
    count = 1
    for val in store:
        val = val[val.index(',')+1:]
        #Base64 is converted to image and saved in image_file as image.jpg
        bytes_decoded = base64.b64decode((val))
        img=Image.open(BytesIO(bytes_decoded))
        out_jpg = img.convert('RGB')
        counter = "%s" %count
        prefix = 'photo'+counter+'.jpg'
        name = os.path.join(dir_path,prefix)
        out_jpg.save(name)
        count+=1



    #image is converted to pdf and saved in pdf_file as Hitesh.pdf
    image_list = []
    for img in os.listdir(dir_path):
        image_list.append(Image.open(os.path.join(dir_path,img)))

    pdf_name = './pdf_file/Hitesh.pdf'
    image_list[0].save(pdf_name,"PDF",resolution =100.0 , save_all= True, append_images = image_list[1:])



    #pdf is converted to base64 format
    with open('./pdf_file/Hitesh.pdf','rb') as imageFile:
        val = base64.b64encode(imageFile.read())
    


    # base64 of pdf is then converted to string so as to send as a reply to the frontend post request
    data['processedpdf'] = val.decode()
    str = 'data:application/pdf;base64,'+data['processedpdf']



    #deleting the temporary folder which is created for storing and converting the images to pdf
    #deleting image folder
    dir_img = os.path.join(path,imageFolder)
    for f in os.listdir(dir_img):
        os.remove(os.path.join(dir_img,f))
    os.rmdir(os.path.join(path,imageFolder))



    #deleting pdf folder
    dir_pdf = os.path.join(path,pdfFolder)
    for f in os.listdir(dir_pdf):
        os.remove(os.path.join(dir_pdf,f))
    os.rmdir(os.path.join(path,pdfFolder))



    # reply sent in JSON format
    return jsonify(str)

if __name__ == '__main__':
    app.run(debug = True, port = 5500)