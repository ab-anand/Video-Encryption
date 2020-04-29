from matplotlib import pyplot as plt 
import cv2 


# img = cv2.imread("frames/res_lena.jpg", 1)
img = cv2.imread("frames/frame_enc_lena.jpg", 1) 
# plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') 

# find frequency of pixels in range 0-255 
# histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.hist(img.ravel(),256,[0,256]) 
# show the plotting graph of an image 
# plt.plot(histr) 
plt.show() 