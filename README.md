## Video Encryption using [Space Filling Curves](https://en.wikipedia.org/wiki/Space-filling_curve) 
![Python 3x](https://img.shields.io/pypi/pyversions/django?color=green&style=plastic)

<p align="center">
  <img src="img.jpg">
</p>
This project is aimed to implement an algorithm to prevent the Chosen Plain Text Attack on Space Filling Curves.  
With the help of that algorithm we would be encrypting videos using Selective Frame Encryption.

---

### Project Tree
```
Video-Encryption/
	├── bin
	│   ├── setup
	│   └── setup.sh
	├── capture_frames.py
	├── decrypt.py
	├── encrypt.py
	├── frame_editor.py
	├── frames
	│   ├── frame0.jpg
	│   ├── frame_dec.jpg
	│   ├── frame_enc_2.jpg
	│   ├── frame_enc_9.jpg
	│   └── frame_enc.jpg
	├── hilbertt.py
	├── img.jpg
	├── input2.avi
	├── input2.mp4
	├── inverted_pixels.json
	├── metrics
	│   ├── correlation.py
	│   ├── entropy.py
	│   ├── hist.py
	│   ├── ncc2.py
	│   ├── plot_cor.py
	│   ├── psnr.py
	│   └── ssim.py
	├── multiprocessing
	│   ├── mulitprocessing.py
	│   └── pooling.py
	├── output.avi
	├── output_dec.avi
	├── pixels.json
	├── playback.mp4
	├── playout.avi
	├── README.md
	├── requirements.txt
	├── resize_frame.py
	├── reverse_pixels.py
	├── SETUP.md
	├── swap.py
	└── video_dec.py

```

### Project Files

* `capture_frames.py` 
	* This files uses OpenCV and other tools to capture a particular frame.
	* It takes the location of the video through commandline arguments.
	* It then capture frames at every 6 seconds interval.
	* Output frames are then saved in the `Frames` folder.
	* The code has been provided with relevant comments for further information.

--- 

### Milestones of the Project

- [x] <b>Capturing Frames</b>
	- <i>Getting particular frames from a given video</i>.
- [x] <b>Strategy for selecting frames</b>
	- <i> Deciding algorithm for selecting frames for `Selective Frame Encryption`</i>.
- [x] <b>Scrambling the frames</b>
	- <i>Using SFCs to encrypt the acquired frame</i>.
- [x] <b>Putting back the Frames</b>
	- <i>Pushing the scrambled frames back in the output video</i>.
- [x] <b>Decrypting it back</b>
	- <i>Converting the scrambled frames back to original frame and create the output video</i>.

---


### Setup

Visit the [Setup file](SETUP.md)