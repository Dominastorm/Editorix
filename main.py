# Importing all the required modules
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from scipy.ndimage import rotate

img_file = "foxy.jpg"
img = np.array(Image.open(img_file))

def display_image(img):
	plt.figure(figsize=(8,8))
	plt.imshow(img)
	plt.show()
	
def rotate_right(img):
	img = np.rot90(img)
	display_image(img)
	return img

def rotate_left(img):
	img = rotate(img, angle = 270)
	display_image(img)
	return img
	
def rotate_by_angle(img, angle):
	img = rotate(img, angle=angle)
	display_image(img)
	return img

def grayscale(img):
	rgb_weights = [0.2989, 0.5870, 0.1140]
	img = np.dot(img[...,:3], rgb_weights)
	plt.imshow(img, cmap=plt.get_cmap("gray"))
	plt.show()
	return img
	
def negative(img):
	img = 255 - img
	plt.imshow(img)
	plt.show()
	return img

def padding(img, width):
	img = np.array(Image.open('foxy.jpg'))
	img = np.pad(img, ((width, width),(width, width),(0,0)), mode='constant')
	display_image(img)
	return img


# make red, green and blue filters
def rgb_channel(img):
	img = np.array(img)
	img_R, img_G, img_B = img.copy(), img.copy(), img.copy()
	img_R[:, :, (1, 2)] = 0
	img_G[:, :, (0, 2)] = 0
	img_B[:, :, (0, 1)] = 0
	img_rgb = np.concatenate((img_R,img_G,img_B), axis=1)
	plt.figure(figsize=(15, 15))
	plt.imshow(img_rgb)
	plt.show()



'''
1. Display Image
2. Rotate Left
3. Rotate Right
4. Rotate By Angle
5. Negative Image
6. Grayscale Image
7. Pad Image
8. Visualize RGB Channels (Don't save image) 
9. Colour Reduction
10. Trim Image
11. Paste image with slice
12. Binarize Image
13. Flip Image
14. Blend Two Images
15. Mask Image
16. Plot Histogram for Pixel Density
0. Quit
'''

choice = 1

while choice != 0: 
	choice = int(input("Enter your choice: "))
	if choice == 1:
		display_image(img)
	elif choice == 2:
		img = rotate_left(img)
	elif choice == 3:
		img = rotate_right(img)
	elif choice == 4:
		direction = input("Enter direction to rotate (r or l): ")
		angle = int(input("Enter angle to rotate by: "))
		if direction == 'l':
			angle = 360 - angle
		img = rotate_by_angle(img, angle)
	elif choice == 5:
		img = negative(img)
	elif choice == 6:
		img = grayscale(img)
	elif choice == 7:
		width = int(input("Enter padding width: "))
		img = padding(img, width)
	elif choice == 8:
		rgb_channel(img)
		
		

