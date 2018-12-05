from skimage import io
import os
import numpy as np
from pathlib import Path

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

picnomarkers = "screenshotnomarkersA.png"

picpath = str(Path.home()) + "/Pictures/"

print("lower number means more similar")

picA = io.imread(picpath + "screenshotA.png")
picB = io.imread(picpath + "screenshotB.png")
picC = io.imread(picpath + "screenshotC.png")

picAnm = io.imread(picpath + "screenshotnomarkersA.png")
picBnm = io.imread(picpath + "screenshotnomarkersB.png")
picCnm = io.imread(picpath + "screenshotnomarkersC.png")

#print(picA, picB)

print("pic A vs pic B:", mse(picA, picB))
print("pic A vs pic C:", mse(picA, picC))
print("pic C vs pic B:", mse(picC, picB))

print("pic Anm vs pic Bnm:", mse(picAnm, picBnm))
print("pic Anm vs pic Cnm:", mse(picAnm, picCnm))
print("pic Cnm vs pic Bnm:", mse(picCnm, picBnm))

print("pic A vs pic Bnm:", mse(picA, picBnm))
print("pic A vs pic Cnm:", mse(picA, picCnm))
print("pic C vs pic Bnm:", mse(picC, picBnm))

print("pic Anm vs pic B:", mse(picAnm, picB))
print("pic Anm vs pic C:", mse(picAnm, picC))
print("pic Cnm vs pic B:", mse(picCnm, picB))

print("end")
