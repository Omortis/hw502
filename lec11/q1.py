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
#         that returns a list or array that flips a biased coin with probability pHeads of heads a total of n times.
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


def countHeads(trialList):

    data = np.array(trialList)

    headsArr = np.extract(data == "H", data)
    tailsArr = np.extract(data == "T", data)

    heads = np.around((headsArr.size / len(trialList)) * 100, 1)
    tails = np.around((tailsArr.size / len(trialList)) * 100, 1)

    print("\n'H': {}%".format(heads))
    print("'T': {}%\n".format(tails))


n = 100000
pHeads = 0.75
trialList = biasedCoinTrial(n, pHeads)

print("Flips : ", n)
print("pHeads: ", pHeads)
countHeads(trialList)
