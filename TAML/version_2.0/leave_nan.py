import numpy as np
def fill_nan(array,ratio):
    where_are_nan=np.isnan(array)
    num=np.sum(where_are_nan)
    init_mean=np.mean(array[num:])
    for i in range(0,num):
        array[i]=np.random.uniform(np.mean(array[num:])-ratio*np.std(array[num:]),np.mean(array[num:])+ratio*np.std(array[num:]))
    return array