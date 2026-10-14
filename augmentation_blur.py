import os
from PIL import Image, ImageFilter

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "images")
output_dir = os.path.join(base_dir, "blur")

os.makedirs(output_dir, exist_ok=True)

blur_radii = [2, 3, 4, 5]

for filename in os.listdir(input_dir):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(input_dir, filename))

    for radius in blur_radii:
        blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))
        blurred.save(os.path.join(output_dir, f"{name}_blur{radius}{ext}"))
