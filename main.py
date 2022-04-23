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
	img = np.pad(img, ((width, width),(width, width),(0,0)), mode='constant')
	display_image(img)
	return img


# make red, green and blue filters
def rgb_channel(img):
	img_R, img_G, img_B = img.copy(), img.copy(), img.copy()
	img_R[:, :, (1, 2)] = 0
	img_G[:, :, (0, 2)] = 0
	img_B[:, :, (0, 1)] = 0
	img_rgb = np.concatenate((img_R,img_G,img_B), axis=1)
	plt.figure(figsize=(15, 15))
	plt.imshow(img_rgb)
	plt.show()

# make into a function with a parameter
def colour_reduction(img):
	img = np.array(img)
	# Making Pixel values discrete by first division by // which gives int and then multiply by the same factor
	img_0 = (img // 64) * 64
	img_1 = (img // 128) * 128
	img_all = np.concatenate((img, img_0, img_1), axis=1)
	plt.figure(figsize=(15, 15))
	plt.imshow(img_all)
	plt.show()

# make into function with parameter
def binarize(img):
	img_64 = (img > 64) * 255
	img_128 = (img > 128) * 255
	fig = plt.figure(figsize=(15, 15))
	img_all = np.concatenate((img, img_64, img_128), axis=1)
	plt.imshow(img_all)

# make into function with parameter
def trim_image(img):
	img = img[128:-128, 128:-128, :]
	plt.imshow(img)
	plt.show()

def pixel_intensity_histogram(img):	
	img_flat = img.flatten()
	plt.hist(img_flat, bins=200, range=[0, 256])
	plt.title("Number of pixels in each intensity value")
	plt.xlabel("Intensity")
	plt.ylabel("Number of pixels")
	plt.show()

def mask(img):
	ones = np.ones((img.shape[0] // 2, img.shape[1] // 2, 3))
	zeros = np.zeros(((img.shape[0] // 4, img.shape[1] // 4, 3)))
	zeros_mid = np.zeros(((img.shape[0] // 2, img.shape[1] // 4, 3)))
	up = np.concatenate((zeros, zeros, zeros, zeros), axis=1)
	middle = np.concatenate((zeros_mid, ones, zeros_mid), axis=1)
	down = np.concatenate((zeros, zeros, zeros, zeros), axis=1)
	mask = np.concatenate((up, middle, down), axis=0)
	mask = mask / 255
	img0 = mask * img
	fig = plt.figure(figsize=(10, 10))
	fig.add_subplot(1, 2, 1)
	plt.imshow(img)
	fig.add_subplot(1, 2, 2)
	plt.imshow(img0)

def paste_with_slice(img, img0):
	src = img.resize((128, 128))
	dst = img0.resize((256, 256)) // 4
	dst_copy = dst.copy()
	dst_copy[64:128, 128:192] = src[32:96, 32:96]
	fig = plt.figure(figsize=(10, 10))
	fig.add_subplot(1, 2, 1)
	plt.imshow(src)
	plt.title('Original')
	fig.add_subplot(1, 2, 2)
	plt.imshow(dst_copy)
	plt.title('Pasted with slice')
	plt.show()

def blend_images(img, img0):
	img0 = img0.resize(img.shape[1::-1]) # resize takes 2 arguments (WIDTH, HEIGHT)
	print(img.dtype)
	# uint8
	dst = (img * 0.6 + img0 * 0.4).astype(np.uint8)   # Blending them in
	plt.figure(figsize=(10, 10))
	plt.imshow(dst)
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
13. Lateral Inversion
14. Blend Two Images
15. Mask Image
16. Plot Histogram for Pixel intensity
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
	elif choice == 9:
		colour_reduction(img)
	elif choice == 10:
		trim_image(img)
	elif choice == 11:
		paste_with_slice(img, img)
	elif choice == 12:
		binarize(img)
	elif choice == 13:
		img = np.fliplr(img)
	elif choice == 14:
		img = blend_images(img)
	elif choice == 15:
		img = mask(img)
	elif choice == 16:
		pixel_intensity_histogram(img)
		

