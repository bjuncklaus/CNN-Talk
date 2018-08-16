from PIL import Image
import os

source_dir = 'inputs_cropped/'
destination_dir = 'inputs_grayscaled/'

if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

files = [f for f in os.listdir(source_dir)]

for f in files:
    print('Found image:', f)
    img = Image.open(source_dir + f).convert('L')
    #img = img.rotate(270, expand=True)
    img.save(destination_dir + f)
