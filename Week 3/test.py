import main
import time

st = time.time()
(main.prime_vanilla(4000))
et = time.time()
print(et-st)

st = time.time()
(main.prime_c(4000))
et = time.time()
print(et-st)