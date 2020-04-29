import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import cv2 

plt.style.use('ggplot')

def plot_corr(x, y):
	x = x.flatten()
	y = y.flatten()
	slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
	line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
	fig, ax = plt.subplots()
	ax.plot(x, y, linewidth=0, marker='s', label='Data points')
	ax.plot(x, intercept + slope * x, label=line)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.legend(facecolor='white')
	plt.show()


def main(): 
    # original = cv2.imread("frames/frame0.jpg") 
    # compressed = cv2.imread("frames/frame_enc_2.jpg", 1) 
    compressed = cv2.imread("frames/frame_enc_lena.jpg", 1) 
    original = cv2.imread("frames/res_lena.jpg", 1) 
    plot_corr(original, compressed) 
    # print(f"PSNR value is {value} dB") 
       
if __name__ == "__main__": 
    main() 