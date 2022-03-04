import deeplabcut
from deeplabcut import auxiliaryfunctions

import random
import numpy as np
import tensorflow as tf


SEED = 47

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
# set random seed for reproduction

if __name__ == '__main__':

    config = "californiamouse-marlerlab-2022-03-03\\config.yaml"

    print(auxiliaryfunctions.read_config(config))
    deeplabcut.extract_frames(config=config,
                              mode='automatic',
                              algo='kmeans')
    
    deeplabcut.label_frames(config=config)
                            # multiple_individualsGUI=True)
#     cfg = auxiliaryfunctions.read_config(config)
#     if cfg.get("multianimalproject", False) or multiple_individualsGUI:
#         from deeplabcut.gui import multiple_individuals_labeling_toolbox

#         multiple_individuals_labeling_toolbox.show(config, config3d, sourceCam)
    
    deeplabcut.create_training_dataset(config=config,
                                       net_type=None,
                                       augmenter_type=None)