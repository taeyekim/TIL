A = list(map(int, input().split()))

A.sort()
cnt = len(A) - 1
total = 0
while cnt > 0:
    total += A[0] * cnt
    A.pop(0)
    cnt -= 1
print(total)