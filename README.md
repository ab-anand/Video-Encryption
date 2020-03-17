## Encryption using [Space Filling Curves](https://en.wikipedia.org/wiki/Space-filling_curve)



### Installation 

#### Use Python 3x

#### Install virtual environment:
```bash
virtualenv -p python3 envname
``` 
#### Activate the environment: 
```bash
source envname/bin/activate
``` 
#### Install the requirements using requirements.txt file: 
```bash
pip install -r requirements.txt
``` 
`$ pip install -r requirements.txt`

#### Run the file: 
```bash
python capture_frames.py playback.mp4
``` 


---

### Milestones of the Project

- [x] <b>Capturing Frames</b>
	- <i>Getting particular frames from a given video</i>.
- [ ] <b>Strategy for selecting frames</b>
	- <i> Deciding technique for selecting frames for `Selective Frame Encryption`.
- [ ] <b>Scrabling the frames</b>
	- <i>Using SFCs to encrypt the acquired frame</i>
- [ ] <b>Putting back the Frames</b>
	- <i>Pushing the scrambled frames back in the output video</i>