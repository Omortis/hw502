import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def retRateAccumulator(w, r,):

    if w == 0:
        return 1
    else:
        return (1 + r) ** (w - 1) + retRateAccumulator(w - 1, r)


def retirementCalc(w, r, savings):
    print("w: ", w)
    print("r: ", r)
    print("savings: ", savings)
    ra = retRateAccumulator(w, r)
    print("ra: ", ra)
    return savings / ra


moneyFmt = "${:,.2f}"

currentAge = 54
retirementAge = 70
deathAge = 100
W = retirementAge - currentAge
R = 0.05
retirementPay = 50000
savings = (deathAge - retirementAge)*retirementPay
print(moneyFmt.format(savings))

M = retirementCalc(W, R, savings)
print(moneyFmt.format(M))
