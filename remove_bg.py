from rembg import remove
from io import BytesIO
import requests
from PIL import Image

def remove_bg(url):

    if url[-4:] == " -bg":
        img = Image.open(BytesIO(requests.get(url[:-4]).content))
        return(img)
        
    img = Image.open(BytesIO(requests.get(url).content))
    return(remove(img))
