import numpy as np
import matplotlib.pyplot as plt
f = np.linspace(0, 1, 100)
#! Part (a)
def f1(f, I=1000, k1=1, k2=1, p=0.6):
    # return [I * (1 + fr * (p * (k1 + k2) - k2)) for fr in f]
    return I * (1 + f * (p * (k1 + k2) - k2))

fig, ax = plt.subplots()
ax.plot(f, f1(f))
ax.set_xlabel("Kelly Fraction 'f'")
ax.set_ylabel("Expected wealth")
fig.suptitle("Expected value of wealth (p=0.6)")
plt.savefig("Q1a.png")
plt.show()

#! Part (b)
def f2(f, I=1000, k1=1, k2=1, p=0.6):
    # return [np.log(I) + p * np.log(1 + k1 * fr)]
    return np.log(I) + p * np.log(1 + k1 * f) + (1 - p) * np.log(1 - k2 * f)

fig, ax = plt.subplots()
ax.plot(f, f2(f))
ax.set_xlabel("Kelly Fraction 'f'")
ax.set_ylabel("Expect log of wealth")
fig.suptitle("Expected log of wealth (p=0.6)")
plt.savefig("Q1b.png")
plt.show()