# CaliforniaMouseDLC

### Overview

The purpose of the repository is to integrate [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) to the pipeline of Marler Lab's research.

### Install
Correct CUDA library needs to be downloaded for GPU access.
DeepLabCut is better to be install separately (git clone version 2.2.0.6 and move library to project source. Other version may not be compatible).

```bash
pip install -r requirements.txt
```

### Usage
The project is run on Windows environment.
```bash
# intialize project
python dlc_init.py --video_dir [VIDEO_DIRECTORY]

# start labeling dataset
python dlc_label.py

# start training model
python dlc_train.py

# generate labeled videos
python dlc_generate.py --video_dir [VIDEO_DIRECTORY]
```