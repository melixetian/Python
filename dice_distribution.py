#!/usr/bin/env python3

"""
Скрипт для изучения распределения значений
при броске 2 игральных костей.
"""

from random import randint

from matplotlib import pyplot as plt


def plotter(y, n):
    x = distr.keys()
    y = distr.values()
    xmax = max(x)
    ymax = max(y)

    plt.plot(x, y)
    plt.grid(True)
    plt.title("Histogram dice distribution")
    plt.xlabel(f"Value (n = {n})")
    plt.ylabel("Probability")
    plt.axis([0, xmax, 0, ymax + 1])
    plt.savefig(f"tests/dice/{n}.png")


if __name__ == "__main__":
    distr = dict()
    for x in range(15):
        distr[x] = 0

    check = 10
    for i in range(1000000):
        x1 = randint(1, 6)
        x2 = randint(1, 6)
        distr[x1 + x2] += 1
        if i == check - 1:
            check *= 10
            plotter(distr, i + 1)
            print(f"{i + 1} is done")
