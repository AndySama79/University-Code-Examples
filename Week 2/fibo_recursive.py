def fibo_recursive(N):
    if N < 2:
        return N
    return fibo_recursive(N - 1) + fibo_recursive(N - 2)

for ii in range(6):
    print(f'F({ii}) = {fibo_recursive(ii)}')