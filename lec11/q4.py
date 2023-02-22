import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def biasedFlip(pHeads):

    biased = np.random.choice(['H', 'T'], size=1, p=[pHeads, 1-pHeads])
    return biased[0]


def biasedCoinTrial(n, pHeads):

    return [biasedFlip(pHeads) for i in range(n)]


def runExperiment(d, n, pHeads):
    results = []

    for i in range(d + 1):

        data = biasedCoinTrial(n, pHeads)

        # Retrieve counts for both H and T
        *_, counts = np.unique(data, return_counts=True)
        # [0]: H
        # [1]: T
        results.append(counts[0])

    return results


heads3 = runExperiment(1000, 100, .2)
heads4 = runExperiment(1000, 100, .5)

df2 = pd.DataFrame({"0.2": heads3, "0.5": heads4})

sns.histplot(
    df2,
    kde=True,
).set(title="d=1000, n=100")

plt.show()
