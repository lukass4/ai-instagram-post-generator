from create_images import new_point_image, new_title_image
from api_requests.ai_api_request import get_response, format
from os import mkdir
from remove_bg import remove_bg
from PIL import Image

question = input("What is the title of the social media post? ")
response = format(get_response(question))
mkdir(question)

confirmation = ""
while confirmation != "y":
    img_url = input("Please supply and image for the title: ")
    new_title_image(question, remove_bg(img_url)).show()
    confirmation = input("Does this look OK? ")
    print(confirmation)
new_title_image(question, remove_bg(img_url)).save(f"{question}\\1.jpeg")

point_no = 2
while point_no < 7:
    point_split = response[point_no-2].split(" - ")
    if len(point_split) == 1:
        point_split = response[point_no-2].split(" – ")
    if len(point_split) == 1:
        point_split = response[point_no-2].split(": ")
    
    img_url = input(f"Please supply an image url for a point titled \"{point_split[0]}\": ")
    new_point_image(point_split[0], point_split[1], remove_bg(img_url)).show()

    confirmation = input("Does this look OK? ")

    if confirmation == "y":
        new_point_image(point_split[0], point_split[1], remove_bg(img_url)).save(f"{question}\\{point_no}.jpeg")
        point_no += 1
    else:
        pass

Image.open("images\\End.png").save(f"{question}\\end.png")