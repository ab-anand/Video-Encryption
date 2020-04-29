import skimage.measure  
import cv2 
import numpy as np   
# entropy = skimage.measure.shannon_entropy(img)


def calc_entropy(orig, enc):
	entropy_org = skimage.measure.shannon_entropy(orig)
	entropy_enc = skimage.measure.shannon_entropy(enc)
	print('Entropy of Original Frame: ', entropy_org)
	print('Entropy of Encrypted Frame: ', entropy_enc)




def main(): 
    # original = cv2.imread("frames/frame0.jpg") 
    # compressed = cv2.imread("frames/frame_enc_2.jpg", 1) 
    compressed = cv2.imread("frames/frame_enc_lena.jpg", 1) 
    original = cv2.imread("frames/res_lena.jpg", 1) 
    calc_entropy(original, compressed) 
    # print(f"PSNR value is {value} dB") 
       
if __name__ == "__main__": 
    main() 