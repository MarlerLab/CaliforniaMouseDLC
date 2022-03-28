# CaliforniaMouseDLC

### Overview

The purpose of the repository is to integrate [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) to the pipeline of Marler Lab's research.

### Install
Correct CUDA library needs to be downloaded for GPU access.

```bash
pip install -r requirements.txt
```

### Usage
```bash
# intialize project
python dlc_init.py --video_dir [VIDEO_DIRECTORY]

# start labeling dataset
python dlc_label.py

# start training model
python dlc_train.py
```