#! /usr/local/bin/python3
# https://www.geeksforgeeks.org/filtering-images-based-size-attributes-python/

from PIL import Image
from shutil import copyfile
import os, os.path
from pathlib import Path

def filterImages(path, thresholdWidth, thresholdHeight):
	print("Welcome")

	# array for identifying image files
	imgs = []
	
	# supported extensions
	valid_images = [".jpg",".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]
	
	# read images into array
	for f in os.listdir(path): 
		ext = os.path.splitext(f)[1]
		
		if ext.lower() not in valid_images:
			continue
		imgs.append(f)
		
	# check for and/or create destination folder
	directory = os.path.dirname(path) + '/archived-trash/'
	
	# something failing here. didn't investigate yet. not sure why but it was silently
	# failing to make the directory. i just created manually. 
	if not os.path.exists(directory):
		os.makedirs(directory)
			
		
	# array for filtered images
	filteredImages = []
	
	for i in imgs:
		image = Image.open(os.path.join(path, i))
		
		# store dimensions
		width, height = image.size
		
		if (width < thresholdWidth and height < thresholdHeight):
			copyfile(os.path.join(path, i), os.path.join(path + '/archived-trash', i))
		
		elif (width < thresholdWidth and height >= thresholdHeight):
			copyfile(os.path.join(path, i), os.path.join(path + '/archived-trash', i))
		
		elif (width >= thresholdWidth and height < thresholdHeight):
			copyfile(os.path.join(path, i), os.path.join(path + '/archived-trash', i))
		
		# so you know its working
		print(image.filename + " " + str(image.size))	
		
		filteredImages.append(i)
		
		
	return filteredImages
	
	

if __name__ == '__main__':
	
	filteredImages = []
	# defaults. should probably take these as paramaters by cba atm. 
	filteredImages = filterImages("/Users/warrenkopp/githubs/desktops", 2560, 1440)