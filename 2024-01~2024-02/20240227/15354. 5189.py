# 15354. 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

def per(k, midSum):
    # if k == N:
    #     print(path)
#         sumV = 0
#         for i in range(N-1):
#             s = path[i]
#             e = path[i+1]
#             sumV += ARR[s][e]
#               print(path, sumV+ARR[e][0])
        return

    for i in range(N):
        if not used[i]:
            path[k] = i
            used[i] = True
            per(k+1, ????)
            used[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    path = [-1] * N
    used = [False] * N

    used[0] = True
    path[0] = 0

    per(1)
