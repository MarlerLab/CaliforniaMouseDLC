import os
import deeplabcut
import utils
from deeplabcut.gui import multiple_individuals_labeling_toolbox

import random
import numpy as np


SEED = 47

random.seed(SEED)
np.random.seed(SEED)
# set random seed for reproduction

if __name__ == '__main__':

    config = utils.load_config()

    multiple_individuals_labeling_toolbox.show(config, None, None)
    deeplabcut.check_labels(config)

    