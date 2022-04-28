# generate videos with trained model

import os
import subprocess
import deeplabcut
import utils

from argparse import ArgumentParser


def compress(from_, to, fps=10):
    """Compress video to lower resolution and fps. 
    Note this is different to implementation in dlc_init.py
    Parameter:
        - from_: input path
        - to: output path
    """
    cmd = f"ffmpeg -i {from_} -vf scale=960:-2,setsar=1:1,fps={fps} -c:v libx264 -c:a copy {to}"
    subprocess.call(cmd)

def set_args():
    parser = ArgumentParser()
    parser.add_argument('input_dir', 
                        type=str,
                        help="Directory of input videos")
    parser.add_argument('output_dir', 
                        type=str,
                        help="Directory of output videos")
    parser.add_argument('--video_type',
                        type=str,
                        default='mp4',
                        help="Video extension")
    parser.add_argument('--gputouse',
                        type=int,
                        default=0,
                        help="GPU name")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    
    config = utils.load_config()    
    args = set_args()
    
    # make output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # get input videos
    input_videos = [os.path.abspath(os.path.join(args.input_dir, vn)) for vn in os.listdir(args.input_dir)
              if vn.split('.')[-1] == args.video_type]
    videos = []
    for iv in input_videos:
        ov = os.path.join(os.path.abspath(args.output_dir), os.path.split(iv)[-1])
        videos.append(ov)
        print(f"Compressing from {iv} to {ov}")
        compress(iv, ov)

    print(f"Analyzing following videos: {videos}")
    
    deeplabcut.analyze_videos(config,
                              videos=videos,
                              videotype=args.video_type,
                              # destfolder=args.output_dir,
                              gputouse=args.gputouse,
                              save_as_csv=True,
                              batchsize=8)

    deeplabcut.create_labeled_video(config,
                                    videos=videos,
                                    videotype=args.video_type,
                                    # destfolder=args.output_dir,
                                    draw_skeleton=True,
                                    trailpoints=1,)    # hope the trailpoints can increase performance

    # deeplabcut.create_video_with_all_detections(config,
    #                                             videos,
    #                                             videotype=args.video_type,
    #                                             displayedbodyparts='all')