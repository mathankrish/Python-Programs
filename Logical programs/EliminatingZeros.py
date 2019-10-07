import numpy as np
a = [10,20,0,30,0,0]
b=list(filter(lambda x: x != 0, a))
#b=np.trim_zeros(a)
print(b)