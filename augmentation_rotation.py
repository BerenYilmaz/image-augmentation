import os
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "images")
output_dir = os.path.join(base_dir, "rotation")

os.makedirs(output_dir, exist_ok=True)

angles = range(30, 360, 30)  # 30, 60, 90, ..., 330

for filename in os.listdir(input_dir):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(input_dir, filename))

    for angle in angles:
        rotated = img.rotate(angle, expand=True)
        rotated.save(os.path.join(output_dir, f"{name}_{angle}{ext}"))
