from rembg import remove
from PIL import Image
input = Image.open("Logo Mega.jpg")
output = remove(input)
output.save("Logo.png")