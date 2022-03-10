import os
import stat
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
    videos = [vn for vn in os.listdir(args.video_dir)
              if vn.split('.')[-1] == args.video_type]
    head, tail = os.path.split(args.video_dir)
    try:
        tmp_dir = os.path.join(head, f"tmp_{tail}")
        os.makedir(tmp_dir)
    except OSError as e:
        e(f"There already exists directory name {tmp_dir}!")
    
    # chmod to exectuable
    os.chmod('./compress.sh', stat.S_IRWXU)
    for vn in videos:
        # compress videos to tmp_{tail} directory
        vp = os.path.join(args.video_dir, vn)
        vp_to = os.path.join(tmp_dir, vn)
        print(f"compress video from {vp} to {vp_to}")
        # os.system(f'./compress.sh {vp} {vp_to}')
    
    raise
    # later take high-quality videos to low-quality videos (using compress.sh)
    # print(videos)

    config = deeplabcut.create_new_project(project="californiamouse", 
                                  experimenter="marlerlab",
                                  videos=videos,
                                  copy_videos=True,
                                  videotype=args.video_type, 
                                  multianimal=True,)
    print(config)
            
    # edit config.yaml

    with open('config_opt.yaml', 'r') as f:
        edits = yaml.safe_load(f)
        # edits['project_path'] = os.path.abspath('californiamouse-marlerlab')
        
    auxiliaryfunctions.edit_config(configname=config, 
                                   edits=edits)
    
    # # rename project directory
    # _, directories, _ = next(os.walk('.'))
    # for d in directories:
    #     if d.startswith('californiamouse-marlerlab'):
    #         os.rename(d, 'californiamouse-marlerlab')
    
    deeplabcut.extract_frames(config=config,
                              mode='automatic',
                              algo='kmeans',
                              userfeedback=False)
