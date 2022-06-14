# Extract outliers, refine labels, and merge datasets.

import os
import subprocess
import deeplabcut
import utils

from argparse import ArgumentParser

def set_args():
    parser = ArgumentParser()
    parser.add_argument('video_dir', 
                        type=str,
                        help="Directory of input videos only (the input directory used in dlc_generate.py)")
    parser.add_argument('analysis_dir', 
                        type=str,
                        help="Directory of analysis files")
    parser.add_argument('--video_type',
                        type=str,
                        default='mp4',
                        help="Video extension")
    parser.add_argument('--outlieralgorithm',
                        type=str,
                        default='uncertain',
                        help="The algorithm used to identify outliers")
    parser.add_argument('--extractionalgorithm',
                        type=str,
                        default='kmeans',
                        help="The algorithm used to extract frames")
    parser.add_argument('--gputouse',
                        type=int,
                        default=0,
                        help="GPU name")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    
    config = utils.load_config()    
    args = set_args()

    # get input videos
    videos = [os.path.abspath(os.path.join(args.analysis_dir, vn)) for vn in os.listdir(args.video_dir)
              if vn.split('.')[-1] == args.video_type]

    print(f"Extracting outlier frames from the following videos: {videos}")
    deeplabcut.extract_outlier_frames(
        config,
        videos=videos,
        videotype=args.video_type,
        outlieralgorithm=args.outlieralgorithm,
        extractionalgorithm=args.extractionalgorithm,
    )
    
    os.system("python dlc_label.py")
    
    print("Merging the refined labels with existing labels")
    deeplabcut.merge_datasets(config)
