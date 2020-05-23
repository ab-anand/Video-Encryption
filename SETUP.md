### Installation

#### The easy way

* Clone the repository
```bash
$ git clone https://github.com/ab-anand/Video-Encryption.git
``` 

* Move inside the folder
```bash
$ cd Video-Encryption
``` 

* Run setup file
```bash
$ bin/setup
``` 

* If the above command doesn't work, try running:
```bash
$ bash bin/setup.sh
``` 

* start the server
```bash
$ python3 capture_frames.py playback.mp4
``` 

---

#### OR (The hard way)

* Install pip
```bash
$ sudo apt-get install python3-pip
```

* Install virtual environment
```bash
$ sudo pip3 install virtualenv
```

* Create virtual environment:
```bash
$ virtualenv -p python3 envname
``` 

* Activate the environment: 
```bash
$ source envname/bin/activate
``` 

* Install the requirements using requirements.txt file: 
```bash
$ pip install -r requirements.txt
``` 