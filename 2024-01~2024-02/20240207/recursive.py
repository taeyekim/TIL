# i 현재위치, k 목표
def f(i, k):
    if i == k:
        print(brr)
    else:
        brr[i] = arr[i]
        print(arr[i])
        f(i+1, k)

arr = [10, 20, 30]
N = len(arr)
brr = [0]*N
f(0, N)

#-----------------
def fib_r(n):
    if n < 2:
        return n

    return fib_r(n-1) + fib_r(n-2)

print(fib_r(5))
#------------------------
n = 5
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

def fib_m(n):
    if n > 1 and memo[n] == 0:
        memo[n] = fib_m(n-1) + fib_m(n-2)

    return memo[n]

print(fib_m(n))

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

