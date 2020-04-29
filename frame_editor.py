import cv2
import json
import time
import numpy as np
from resize_frame import res
from PIL import Image, ImageEnhance
from hilbertcurve.hilbertcurve import HilbertCurve

p=10; N=2

hilbert_curve = HilbertCurve(p, N)


def frame_edit(frame):
    # Convert cv2 image to rgb and load from numpy array
    # print(frame.ndim)
    # print(c_fr.shape)
    # s_time = time.time()
    res_frame = res(frame, 1024, 1024)
    hilbert_pixels = load_hilbert()
    # print(time.time()-s_time)
    enc_frame = scramble_frame(hilbert_pixels, res_frame, 1024)
    count = 7
    # Convert back to bgr numpy array and write to disk
    cv2.imwrite('frames/swap/enc_shot22.png', enc_frame)
    # print(time.time()-s_time)
    # return enc_frame


def load_hilbert():
    with open('pixels.json') as f:
      data = json.load(f)
    return data


def scramble_frame(pix_dic, org_frame, width):
    new_frame = np.copy(org_frame)
    count = 0
    for key, value in pix_dic.items():
        row = int(key)//width
        col = int(key)%width
        # print(row, col)     
        try:      
            new_frame[value[0]][value[1]] = org_frame[row][col]
            count += 1
        except ValueError as v:
            print(str(v))
    print(count)
    return new_frame


def print_frame(frame):
    print(frame.shape)
    print(type(frame))
    print(frame[0][0])


path = cv2.imread('frames/swap/enc_shot2.png', cv2.IMREAD_UNCHANGED)
frame_edit(path)
print_frame(path)
