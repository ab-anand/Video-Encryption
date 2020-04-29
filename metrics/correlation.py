from scipy import signal
import numpy as np
import pandas as pd
import cv2 
# cor = signal.correlate2d (im1, im2)

def calc_corr(orig, enc):
	# cor = signal.correlate2d (orig, enc)
	orig = pd.Series(orig.flatten())
	enc = pd.Series(enc.flatten())
	a = orig.corr(enc)
	b = enc.corr(orig)
	print(a, b)
	# cor = np.corrcoef(orig, enc)
	# print('Correlation: ', cor.shape)




def main(): 
    # original = cv2.imread("frames/frame0.jpg") 
    # compressed = cv2.imread("frames/frame_enc_2.jpg", 1) 
    compressed = cv2.imread("frames/frame_enc_lena.jpg", 1) 
    original = cv2.imread("frames/res_lena.jpg", 1) 
    calc_corr(original, compressed) 
    # print(f"PSNR value is {value} dB") 
       
if __name__ == "__main__": 
    main() 