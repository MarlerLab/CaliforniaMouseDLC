import os
import stat
import shutil
import subprocess
import yaml
import deeplabcut
import utils

from argparse import ArgumentParser
from deeplabcut import auxiliaryfunctions


def compress(from_, to, fps=10):
    """Compress video to lower resolution and fps
    Parameter:
        - from_: input path
        - to: output path
    """
    cmd = f"ffmpeg -ss 00:00:10 -i {from_} -vf scale=960:-2,setsar=1:1,fps={fps} -c:v libx264 -c:a copy {to}"
    subprocess.call(cmd)
    
    
def set_args():
    parser = ArgumentParser()
    parser.add_argument('--video_dir',
                        type=str,
                        required=True,
                        help="PATH TO VIDEO DIRECTORY")
    parser.add_argument('--video_type',
                        default='mp4',
                        type=str,
                        help="TYPE OF VIDEO (mp4/avi)")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = set_args()
    videos = [vn for vn in os.listdir(args.video_dir)
              if vn.split('.')[-1] == args.video_type]
    head, tail = os.path.split(args.video_dir)
    try:
        tmp_dir = os.path.join(head, f"tmp_{tail}")
        os.makedirs(tmp_dir)
    except OSError as e:
        e(f"There already exists directory name {tmp_dir}!")
        raise
    
    for vn in videos:
        # compress videos to tmp_{tail} directory
        vp = os.path.join(args.video_dir, vn)
        vp_to = os.path.join(tmp_dir, vn)
        print(f"compress video from {vp} to {vp_to}")
        compress(vp, vp_to)
        
    videos = [os.path.join(tmp_dir, vn) for vn in videos]

    config = deeplabcut.create_new_project(project="californiamouse", 
                                  experimenter="marlerlab",
                                  videos=videos,
                                  copy_videos=True,
                                  videotype=args.video_type, 
                                  multianimal=True,)
    print(config)
    shutil.rmtree(tmp_dir)
            
    # edit config.yaml
    with open('config_opt.yaml', 'r') as f:
        edits = yaml.safe_load(f)
    auxiliaryfunctions.edit_config(configname=config, 
                                   edits=edits)
    
    deeplabcut.extract_frames(config=config,
                              mode='automatic',
                              algo='kmeans',
                              userfeedback=False)
