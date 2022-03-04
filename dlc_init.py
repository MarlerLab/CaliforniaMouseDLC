import os
import yaml
import deeplabcut

from argparse import ArgumentParser
from deeplabcut import auxiliaryfunctions

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
    videos = [os.path.join(args.video_dir, vn) for vn in os.listdir(args.video_dir)
              if vn.split('.')[-1] == args.video_type]

    # later take high-quality videos to low-quality videos (using compress.sh)
    # print(videos)

    config = deeplabcut.create_new_project(project="californiamouse", 
                                  experimenter="marlerlab",
                                  videos=videos,
                                  copy_videos=True,
                                  videotype=args.video_type, 
                                  multianimal=True,)

    # edit config.yaml

    with open('config_opt.yaml', 'r') as f:
        try:
            edits = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)

    auxiliaryfunctions.edit_config(configname=config, 
                                   edits=edits)