import cv2


def res(img, width, height):
	# print('Original Dimensions : ',img.shape)

	dim = (width, height)

	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	 
	# print('Resized Dimensions : ',resized.shape)
	# cv2.imwrite('frames/swap/enc_shot3.png', resized)

	return resized


# frame = cv2.imread('frames/swap/shot3.png', cv2.IMREAD_UNCHANGED)
# res(frame, 1024,1024)
