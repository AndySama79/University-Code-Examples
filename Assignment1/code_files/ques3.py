import numpy as np
import matplotlib.pyplot as plt
f = np.linspace(0, 1, 100)
#!  Part(a)
def exp(f, I=1000, k1=1, k2=1, p=0.6):
    # return [np.log(I) + p * np.log(1 + k1 * fr)]
    return np.log(I) + p * np.log(1 + k1 * f) + (1 - p) * np.log(1 - k2 * f)

def var(f, I=1000, k1=1, k2=1, p=0.6):
    return p * (np.log(I * (1 + k1 * f))) ** 2 + (1 - p) * (np.log(I * (1 - k2 * f))) ** 2 - (np.log(I) + p * np.log(1 + k1 * f) + (1 - p) * np.log(1 - k2 * f)) ** 2

fig, ax = plt.subplots()
ax.plot(f, exp(f))
ax.plot(f, var(f))
ax.set_xlabel("Kelly Fraction 'f'")
ax.set_ylabel("Expected Log Wealth / Variance of Log Wealth")
ax.legend(["Expectation", "Variance"])
fig.suptitle("Expectation and Variance of Log Wealth")
plt.savefig("Q3a.png")
plt.show()

#!  Part(b)