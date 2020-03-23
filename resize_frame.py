import cv2


def res(img, width, height):
	# print('Original Dimensions : ',img.shape)

	dim = (width, height)

	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	 
	# print('Resized Dimensions : ',resized.shape)

	return resized


# frame = cv2.imread('frames/frame0.jpg', cv2.IMREAD_UNCHANGED)
# res(frame)
