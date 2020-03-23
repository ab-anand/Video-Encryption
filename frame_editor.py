import cv2
import json
import numpy as np
from resize_frame import res
from PIL import Image, ImageEnhance
from hilbertcurve.hilbertcurve import HilbertCurve

p=10; N=2

hilbert_curve = HilbertCurve(p, N)


def frame_edit(frame):
    # Convert cv2 image to rgb and load from numpy array
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # img = Image.fromarray(frame)
    # print(frame.ndim)
    # print(c_fr.shape)
    res_frame = res(frame, 1024, 1024)
    hilbert_pixels = load_hilbert()
    enc_frame = scramble_frame(hilbert_pixels, res_frame, 1024)
    # enc_frame = res(enc_frame, 1280, 720)
    # c_fr[719][1279] = [25, 34, 24]
    # print(c_fr[719][1279])

    # Convert back to bgr numpy array and write to disk
    # cv2.imwrite('frames/frame_enc_{}.jpg'.format(str(count)),enc_frame)

    return enc_frame


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
            pos = hilbert_curve.distance_from_coordinates([row, col])       
            new_frame[value[0]][value[1]] = org_frame[row][col]
            # new_frame[row][col] = org_frame[value[0]][value[1]]
            count += 1
        except ValueError as v:
            print(str(v))
    print(count)
    return new_frame


def print_frame(frame):
    print(frame.shape)
    # print(len(frame[0]))
    # print(frame[1][0])


# path = cv2.imread('frames/frame0.jpg', cv2.IMREAD_UNCHANGED)
# frame_edit(path)
# print_frame(path)
# scramble_frame(path)