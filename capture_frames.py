import cv2 
import time
import sys
  

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
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        curr_time = time.time()

        # Getting the current position of the video file(time) and converting it to seconds.
        fr = int(vidObj.get(0))//1000

        # Saves the frames with frame-count with at every 6 second interval 
        if fr%6 == 0:
            print(fr)
            cv2.imwrite("frames/frame%d.jpg" % (count), image)   
  
        count += 1
        # time.sleep(5)
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(vid_path)