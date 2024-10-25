import matplotlib.pyplot as plt
import numpy as np
import roman
from math import ceil, floor 
from DataClasses import DataPoint

def createplot(data: DataPoint) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.xaxis.label.set_fontsize(18)
    ax.yaxis.label.set_fontsize(18)
    ax.yaxis.set_tick_params(labelsize = 14)
    ax.xaxis.set_tick_params(labelsize = 14)
    plt.rcParams.update({'font.size': 24})
    fig.set_size_inches(18,10)
    ax.grid()
    ax.plot(
    [i.period for i in data],
    [i.value for i in data]
    )
    tickLabels = [roman.toRoman(i) for i in range(1, 13)]
    fig.set_linewidth(18)
    ax.set(
        yticks = np.arange(
            floor(min(data, key = lambda x: x.value).value),
            ceil(max(data, key = lambda x: x.value).value) + 1
            ),
        xticks = np.arange(1, 13),
        xticklabels = tickLabels,
        xlabel = 'Miesiąc',
        ylabel = 'Wartość [%]',
        title = 'Wartość inflacji w roku 2022'
    )
    return fig