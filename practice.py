T = int(input())

import math
while T > 0:
    N, M = map(int, input().split())
    if M >= N:
        print(math.factorial(M) // math.factorial(M-N) // math.factorial(N))
    else:
        print(0)
    T -= 1