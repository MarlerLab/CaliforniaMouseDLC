from argparse import ArgumentParser
import deeplabcut
import utils


config = utils.load_config()



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
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = set_args()
    
    # possibly set pose_cfg.yaml
    
    
    deeplabcut.create_training_dataset(config=config, 
                                       net_type=None, 
                                       augmenter_type=None)
    
    deeplabcut.train_network(config,
                             max_snapshots_to_keep=5,
                             displayiters=args.displayiters,
                             saveiters=args.saveiters,
                             maxiters=args.maxiters,
                             gputouse=args.gputouse)
    
    deeplabcut.evaluate_network(config,
                            plotting=True,
                            gputouse=args.gputouse)
    