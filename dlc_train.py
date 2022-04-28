import os
import argparse
import pandas as pd
import deeplabcut
import utils

from argparse import ArgumentParser
from deeplabcut import auxiliaryfunctions




def set_args():
    parser = ArgumentParser()
    parser.add_argument('--gputouse', 
                        default=0,
                        type=int)
    parser.add_argument('--displayiters', 
                        default=100,
                        type=int)
    parser.add_argument('--saveiters', 
                        default=10_000,
                        type=int)
    parser.add_argument('--maxiters', 
                        default=100_000,
                        type=int)
    parser.add_argument('--train',   # --no-train for False
                        # action=argparse.BooleanOptionalAction,
                        default=True)
    parser.add_argument('--eval',     # --no-eval for False 
                        # action=argparse.BooleanOptionalAction,
                        default=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = set_args()
    print(args)
    
    config = utils.load_config()
    # possibly set pose_cfg.yaml
    
    if args.train:
    
        deeplabcut.create_training_dataset(config=config, 
                                           net_type=None, 
                                           augmenter_type=None)

        deeplabcut.train_network(config,
                                 max_snapshots_to_keep=5,
                                 displayiters=args.displayiters,
                                 saveiters=args.saveiters,
                                 maxiters=args.maxiters,
                                 gputouse=args.gputouse)

    if args.eval:
        deeplabcut.evaluate_network(config,
                                plotting=True,
                                gputouse=args.gputouse)

        # get the best model
        df = pd.read_csv(os.path.join(os.path.split(config)[0], 
                                      "evaluation-results", 
                                      "iteration-0", 
                                      "CombinedEvaluation-results.csv"))

        maxidx = df[' Test error(px)'].idxmax()
        print(f"Best model found with {df[' Test error(px)'][maxidx]} test error(px)")
        auxiliaryfunctions.edit_config(config,
                                       edits={
                                           'snapshotindex': maxidx,
                                       })

    