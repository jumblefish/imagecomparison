# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from pathlib import Path

def mse(imageA, imageB): #implmented in pyskel
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

picnomarkers = "screenshotnomarkersA.png"

picpath = str(Path.home()) + "/Pictures/"

picAnm = cv2.imread(picpath + "screenshotnomarkersA.png")
picA = cv2.imread(picpath + "screenshotA.png")
picBnm = cv2.imread(picpath + "screenshotnomarkersB.png")
picB = cv2.imread(picpath + "screenshotB.png")
picCnm = cv2.imread(picpath + "screenshotnomarkersC.png")
picC = cv2.imread(picpath + "screenshotC.png")


picA = cv2.cvtColor(picA, cv2.COLOR_BGR2GRAY)
picAnm = cv2.cvtColor(picAnm, cv2.COLOR_BGR2GRAY)
picB = cv2.cvtColor(picB, cv2.COLOR_BGR2GRAY)
picBnm = cv2.cvtColor(picBnm, cv2.COLOR_BGR2GRAY)
picC = cv2.cvtColor(picC, cv2.COLOR_BGR2GRAY)
picCnm = cv2.cvtColor(picCnm, cv2.COLOR_BGR2GRAY)

difvalue = ssim(picA, picAnm) #1 is same, -1 is totally different
print("dif between A and Anm:")
print(difvalue)

print("pic A vs pic B:    ", ssim(picA, picB))
print("pic A vs pic C:    ", ssim(picA, picC))
print("pic C vs pic B:    ", ssim(picC, picB))

print("pic Anm vs pic Bnm:", ssim(picAnm, picBnm))
print("pic Anm vs pic Cnm:", ssim(picAnm, picCnm))
print("pic Cnm vs pic Bnm:", ssim(picCnm, picBnm))

print("pic A vs pic Bnm:  ", ssim(picA, picBnm))
print("pic A vs pic Cnm:  ", ssim(picA, picCnm))
print("pic C vs pic Bnm:  ", ssim(picC, picBnm))

print("pic Anm vs pic B:  ", ssim(picAnm, picB))
print("pic Anm vs pic C:  ", ssim(picAnm, picC))
print("pic Cnm vs pic B:  ", ssim(picCnm, picB))

y=0
h=200
x=0
w=1900
#crops the images for comparison
print("pic A vs pic B:crp: ", ssim(picA[y:y+h,x:x+w], picB[y:y+h,x:x+w]))
print("pic A vs pic C:crp: ", ssim(picA[y:y+h,x:x+w], picC[y:y+h,x:x+w]))
print("pic C vs pic B:crp: ", ssim(picC[y:y+h,x:x+w], picB[y:y+h,x:x+w]))

print("pic Anm vs pic B:crp", ssim(picAnm[y:y+h,x:x+w], picB[y:y+h,x:x+w]))
print("pic Anm vs pic C:crp", ssim(picAnm[y:y+h,x:x+w], picC[y:y+h,x:x+w]))
print("pic Cnm vs pic B:crp", ssim(picCnm[y:y+h,x:x+w], picB[y:y+h,x:x+w]))

print("end")
