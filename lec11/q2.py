import os
import numpy as np

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Question 1 - Biased Coin Flips

# Write three functions

#     biasedFlip(pHeads)
#         that returns H with probability pHeads and T with probability 1-pHeads, and
#
#     biasedCoinTrial(n,pHeads)
#         that returns a list or array that flips a biased coin with probability
#         pHeads of heads a total of n times.
#
#     countHeads(trial)
#         that counts the number of heads in the list produced by biasedCoinTrial


def biasedFlip(pHeads):
    """Returns H with probability bHeads, and T with
    probability 1-bHeads."""

    biased = np.random.choice(['H', 'T'], size=1, p=[pHeads, 1-pHeads])

    return biased[0]


def biasedCoinTrial(n, pHeads):
    """Calls biasedFlip n times with H probability pHeads and
    returns a list containing the results."""

    results = []

    for i in range(n + 1):

        results.append(biasedFlip(pHeads))

    return results


def runExperiment(d, n, heads):
    """ d: number of experiments
        n: number of flips per experiemtn
        pHeads: weight for heads"""

    results = []

    for i in range(d + 1):

        data = biasedCoinTrial(n, pHeads)

        # Retrieve counts for both H and T
        *_, counts = np.unique(data, return_counts=True)
        results.append(counts[0])

    return results


d = 1000
n = 100
pHeads = 0.2

heads = runExperiment(d, n, pHeads)
print(heads)
