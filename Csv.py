import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *

d=pd.read_csv('/Users/joebrakoniecki/github/Plot9/Sales Data.csv')
d

interval = []

for i in range(1,len(d.index)+1):
    interval.append(i)

interval
d['Interval'] = interval

d

ggplot(d,aes(x = 'Interval',y = 'Sales Figures')) + geom_point(shape = 'x') + geom_line(linetype = 'dotted') + stat_smooth(method = 'lm')
