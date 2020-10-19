from PIL import Image

img = Image.open('baby.jpeg')

img2 = Image.open('cute-baby.jpg')

img1_resized = img.resize((480, 480))

r, g, b = img1_resized.split()

r1, g1, b1 = img2.split()

new_img = Image.merge('RGB', (r1, g, b1))

new_img.show()
