from PIL import Image, ImageFont, ImageDraw
import textwrap
from remove_bg import remove_bg

def new_title_image(title, image):
    im = Image.open("images\\title_image.png")
    W, H = im.size
    d = ImageDraw.Draw(im)

    title_f = ImageFont.truetype("fonts\\Jost-VariableFont_wght.ttf", 96)

    title_lines = textwrap.wrap(title, width=15)

    d.multiline_text((375, H/2-50), "\n".join(title_lines), anchor="mm", align="center", fill="black", font=title_f)

    image = image.convert("RGBA")
    image_width = round((250/image.size[0])*image.size[1])

    image = image.resize((250, image_width))
    im.paste(image, (W-image_width-50,50), image)


    return(im)

def new_point_image(title, text, image):
    im = Image.open("images\\post_image.png")
    W, H = im.size
    d = ImageDraw.Draw(im)

    title_f = ImageFont.truetype("fonts\\Jost-VariableFont_wght.ttf", 52)
    text_f = ImageFont.truetype("fonts\\Jost-VariableFont_wght.ttf", 28)

    title_lines = textwrap.wrap(title, width=40)
    text_lines = textwrap.wrap(text, width=75)

    d.multiline_text((W/2, 30), "\n".join(title_lines), anchor="ma", align="center", fill="black", font=title_f)
    d.multiline_text((W/2, H/2), "\n".join(text_lines), anchor="mm", align="center", fill="black", font=text_f)

    image = image.convert("RGBA")
    image_width = round((175/image.size[0])*image.size[1])

    image = image.resize((175, image_width))
    im.paste(image, (750,150), image)

    return(im)
