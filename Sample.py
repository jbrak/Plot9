import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *

%matplotlib inline
mpg.head()

ggplot(mpg) + geom_bar(aes(x='class', fill = 'drv')) + theme_bw()
