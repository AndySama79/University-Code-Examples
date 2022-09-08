def fibo_iterative(N):
    
    if N < 2:
        return N
    else:
        F = []
        F.append(0)
        F.append(1)

        for i in range(2, N+1):
            F.append(F[i-1] + F[i-2])
    
    return F[N]

# for i in range(6):
#     print(fibo_iterative(i))