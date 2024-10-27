import matplotlib.pyplot as plt
import numpy as np
from math import ceil, floor 
from DataClasses import *

def createplot(data: DataPoint) -> plt.Figure:
    fig, ax = plt.subplots()
    fig.set_size_inches(6,4)
    ax.grid()
    plotLines = convertData(data)
    for line in plotLines:
        ax.plot(
            [line.firstPeriod, line.secondPeriod],
            [line.firstValue, line.secondValue],
            color = line.color
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