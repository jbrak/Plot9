import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *



d = {'goals' : [49,44,43,36,40,39,29,21,28,30,33,26],'position' : [1,2,3,4,5,6,7,8,9,10,11,12]}


df = pd.DataFrame(d)
df.head()


ggplot(df,aes(x = 'goals', y = 'position')) + geom_point() + geom_smooth(method = 'lm')
