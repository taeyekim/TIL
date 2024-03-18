# 15027. 4869 종이붙이기

T = int(input())

def func(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return func(N - 10)+(2 * func(N - 20)) # 1 3 5 11 21 ...

for tc in range(1, T+1):
    N = int(input())
    cnt = func(N)
    print(f"#{tc} {cnt}")