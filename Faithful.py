import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *


ggplot(faithfuld,aes(x = 'eruptions', y = 'density', fill = 'waiting')) + geom_point(size = 4)
