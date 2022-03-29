# generate videos with trained model


import deeplabcut
import utils

import os

config = utils.load_config()
from easydict import EasyDict as edict
args = edict({
    'video_dir': 'californiamouse-marlerlab-2022-03-12/videos/',
    'video_type': 'mp4',
    'gputouse': 0,
})

# get videos
videos = [os.path.abspath(os.path.join(args.video_dir, vn)) for vn in os.listdir(args.video_dir)
          if vn.split('.')[-1] == args.video_type]

print(videos)
videos = videos[2:3]
print("printing videos")
print(videos)
deeplabcut.analyze_videos(config,
                          videos=videos,
                          videotype=args.video_type,
                          gputouse=args.gputouse,
                          save_as_csv=True,
                          batchsize=4,)
                          
    # deeplabcut.create_labeled_video?
# deeplabcut.create_labeled_video(config,
#                                 videos=videos,
#                                 videotype="mp4",
#                                 draw_skeleton=True,
#                                 trailpoints=1,)    # hope the trailpoints can increase performance

deeplabcut.create_video_with_all_detections(config,
                                            videos,
                                            videotype=args.video_type,
                                            displayedbodyparts='all')