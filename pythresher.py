import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

#this finds all matches of a template and hilights them. 
#there seems to be some problem with the threshold as some matches overlap

#set paths
picpath = str(Path.home()) + "/Pictures/"
picA = picpath + "screenshotA.png"
marker = picpath + "bluemarker.png"

#convert to grayscale
img_rgb = cv2.imread(picA)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#sets the template, height and width
template = cv2.imread(marker,0)
w, h = template.shape[::-1]

#res is a list of minmax values?
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
print(type(res), res) #res is a numpy array?
print(cv2.minMaxLoc(res))#returns most different, most similar matches 
print(res[752,32], res[57,371])#res uses pixel locations as index numbers
threshold = 0.9
loc = np.where( res >= threshold)
print(type(loc), loc)
for pt in zip(*loc[::-1]):
    print(pt)#these are the matching objects?
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)
