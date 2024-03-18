# 15350. 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
import math

def solve(s):
    answer = ''
    cnt = 0
    i = 1 / 2
    while s > 0:
        cnt += 1
        if cnt == 13:
            return "overflow"

        answer = answer + str(math.floor(s // i))
        s = s - int(answer[-1]) * i
        i = i / 2
    return answer

T = int(input())

for tc in range(1, T+1):
    s = float(input())
    print(f"#{tc} {solve(s)}")

