import cv2
import json
import numpy as np
from resize_frame import res
from hilbertcurve.hilbertcurve import HilbertCurve

p=10; N=2

hilbert_curve = HilbertCurve(p, N)


def load_hilbert():
    with open('inverted_pixels.json') as f:
      data = json.load(f)
    # pix_dic = json.load("pixels.json")
    # print(data[str(0)][0])
    return data

def get_pixels(enc_frame, width):
	org_frame = np.copy(enc_frame)
	count = 0
	for i in range(500000):
		row = i//width
		col = i%width
		coords = [row, col]
		try:
			pos = hilbert_curve.distance_from_coordinates(coords)
			# print(coords, pos)
			row_n = pos//width
			col_n = pos%width
			org_frame[row][col] = enc_frame[row_n][col_n]
			count += 1
		except ValueError as v:
			print(str(v))
			# pass
	print(count)

	cv2.imwrite('frames/frame_dec.jpg', org_frame)



def get_pixels_json(enc_frame, width):
	pix_dic = load_hilbert()
	new_frame = np.copy(enc_frame)
	count = 0
	pos = 0
	for key, value in pix_dic.items():
		row = int(key)//width
		col = int(key)%width
		# print(row, col)     
		# pos = hilbert_curve.distance_from_coordinates([row, col])       
		new_frame[value[0]][value[1]] = enc_frame[row][col]
		# new_frame[row][col] = org_frame[value[0]][value[1]]
		count += 1
	print(count)
	new_frame = res(new_frame, 1280, 720)
	# cv2.imwrite('frames/frame_dec.jpg', new_frame)
	return new_frame


# enc_frame = cv2.imread('frames/frame_enc_9.jpg', cv2.IMREAD_UNCHANGED)
# enc_frame = res(enc_frame, 1024, 1024)
# get_pixels(enc_frame, 1280)
# get_pixels_json(enc_frame, 1024)