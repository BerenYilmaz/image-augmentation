import os
from PIL import Image, ImageEnhance

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "images")
output_dir = os.path.join(base_dir, "contrast")

os.makedirs(output_dir, exist_ok=True)

contrast_levels = {
    "high": 1.5,
    "low": 0.5,
}

for filename in os.listdir(input_dir):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(input_dir, filename))
    enhancer = ImageEnhance.Contrast(img)

    for label, factor in contrast_levels.items():
        adjusted = enhancer.enhance(factor)
        adjusted.save(os.path.join(output_dir, f"{name}_{label}{ext}"))
