from PIL import Image
import base64
from io import BytesIO

data = open('base64.txt','r').read()
bytes_decoded = base64.b64decode(data)

img=Image.open(BytesIO(bytes_decoded))
out_jpg = img.convert('RGB')
out_jpg.save('image.jpg')