import numpy as np

x=np.random.random((5,5))
y=(x-x.mean())/x.std()
