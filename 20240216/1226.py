# 1226. [S/W 문제해결 기본] 7일차 - 미로1

# def bfs(s):
#     Q = []
#     visited = [False] * (N+1)
#
#     Q.append(s)
#     visited[s] = True
#     while Q:
#         v = Q.pop(0)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = True

def bfs(stR, stC):
    Q = []
    visited = [[False] * N for _ in range(N)] # 0으로 초기화
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # direction[0]~[3]
    Q.append((stR, stC)) # Q = [], Q.append(stR, stC) Q[0] Q[1]
    visited[stR][stC] = True # 1로 체인지 가능
    
    while Q:
        # v = Q.pop()
        # vR = v[0]
        # vC = v[1]

        vR, vC = Q.pop(0)
        for dr, dc in direction: # (1, 1) + (1, 0) = (2, 1)
            wR = vR + dr
            wC = vC + dc

            if 0 <= wR < N and 0 <= wC < N:
                if arr[wR][wC] == 3:
                    return 1

                if arr[wR][wC] == 0 and not visited[wR][wC]:
                    Q.append((wR, wC))
                    visited[wR][wC] = True # visited[vR][vC] + 1
    return 0

T = 10

for _ in range(1, T+1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    # for row in range(N):
    #     for col in range(N):
    #         if arr[row][col] == 2:
    #             stR = row
    #             stC = col
    #             break

    for row in range(N):
        if arr[row].count(2):
            stC = arr[row].index(2)
            break
    stR = row

    # print(stR, stC)
    print(f"#{tc} {bfs(stR, stC)}")

