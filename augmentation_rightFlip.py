import os
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "images")
output_dir = os.path.join(base_dir, "flip")

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    img = Image.open(os.path.join(input_dir, filename))
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save(os.path.join(output_dir, filename))
