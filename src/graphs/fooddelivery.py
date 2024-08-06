import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


def get_chance_minute(x):
    if (7 * 60) <= x < (8 * 60):
        return 2 / (24 * 60)

    if (12 * 60) <= x < (13 * 60):
        return 2 / (24 * 60)

    if (18 * 60) <= x < (20 * 60):
        return 7 / (24 * 120)

    return 13 / (24 * 20 * 60)


def get_data_frame():
    minutes = range(0, 24 * 60)
    time = []
    p = []
    for t in minutes:
        p.append(get_chance_minute(t) / 7)
        time.append(t)

    print(sum(p))

    data = {'time': time, 'p': p}
    df = pd.DataFrame(data)

    return df


def print_food_ordering():
    df = get_data_frame()
    sns.set_style("darkgrid")
    sns.set_context("paper", rc={"grid.linewidth": 0.6})
    plot = sns.lineplot(data=df, x="time", y="p")
    plot.set(xlabel="time of day", ylabel="probability of ordering food per minute")
    plt.yticks(np.arange(0, 0.0005, step=0.00005))
    plt.xticks(np.arange(0, 24 * 60 + 1, step=120))

    x_labels = []

    for x in plot.get_xticks():
        hour = int(x / 60)
        x_labels.append(f"{hour}")

    plot.set_xticklabels(x_labels)
    plt.show()
    fig = plot.get_figure()
    fig.savefig("food_ordering_distribution.png")


print_food_ordering()
