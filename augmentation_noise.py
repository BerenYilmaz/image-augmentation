import os
import numpy as np
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "images")
output_dir = os.path.join(base_dir, "noise")

os.makedirs(output_dir, exist_ok=True)

noise_strength = 25

for filename in os.listdir(input_dir):
    img = Image.open(os.path.join(input_dir, filename)).convert("RGB")
    arr = np.array(img).astype(np.int16)

    noise = np.random.normal(0, noise_strength, arr.shape)
    noisy_arr = np.clip(arr + noise, 0, 255).astype(np.uint8)

    noisy_img = Image.fromarray(noisy_arr)
    noisy_img.save(os.path.join(output_dir, filename))
