import cv2
import time

def swap_pixels(frame, shape):
	t = time.time()
	for x in range(shape[0]):
		for y in range(shape[1]):
			frame[x][y][0], frame[x][y][2] = frame[x][y][2], frame[x][y][0]
	cv2.imwrite('frames/swap_enc_shot3.png', frame)
	print(time.time()-t)







frame = cv2.imread('frames/swap/swapped_dec3.png', cv2.IMREAD_UNCHANGED)
# print(frame.shape[0])
# print(frame[0][1])
# frame[0][1][0], frame[0][1][2] = frame[0][1][2], frame[0][1][0]
# res(frame, 1024,1024)
swap_pixels(frame, frame.shape)