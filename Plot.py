import matplotlib.pyplot as plt
import numpy as np
from math import ceil, floor 

def createplot(data):
    fig, ax = plt.subplots()
    fig.set_size_inches(6,4)
    ax.grid()
    ax.plot(
    [i.period for i in data],
    [i.value for i in data]
    )
    ax.set(
        yticks = np.arange(
            floor(min(data, key = lambda x: x.value).value),
            ceil(max(data, key = lambda x: x.value).value) + 1
            ),
        xticks = np.arange(1, 13),
        xlabel = 'miesiąc',
        ylabel = 'wartość [%]',
        title = 'wartość inflacji w roku 2022'
    )
    return fig