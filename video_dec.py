import cv2 
import time
import sys
from frame_editor import frame_edit
from resize_frame import res
from decrypt import get_pixels_json

vid_path = str(sys.argv[1])


# Function to extract frames 
def FrameCapture(path): 
    '''This func takes the 
    video path as input and 
    captures the frame at every 
    six seconds interval and
    saves the frame in Frames folder
    '''
      
    start_time = time.time()

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # frame rate
    fps = vidObj.get(cv2.CAP_PROP_FPS)

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = 1280
    frame_height = 720

    # fourcc
    fourcc = vidObj.get(cv2.CAP_PROP_FOURCC)
    # print(fourcc)
    # output video file
    out = cv2.VideoWriter('output_dec.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 

        # Getting the current position of the video file(time) and converting it to seconds.
        fr = int(vidObj.get(0))//1000

        # Saves the frames with frame-count with at every 6 second interval 
        # if fr%4 == 0:
        #     if success:
        #         image = get_pixels_json(image, 1024)
        # else:
        #     image = res(image, 1280, 720)
        #     print(fr)
        #     cv2.imwrite("frames/frame%d.jpg" % (count), image)   
        # image = frame_edit(image, count)

        if success:
            image = get_pixels_json(image, 1024)
        
        count += 1
        out.write(image)
        # count += 1
        # break
    print("Time taken to encrypt = {}".format(time.time()-start_time))
    print("Number of frames = {}".format(count))
    vidObj.release()
    out.release()

  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(vid_path)