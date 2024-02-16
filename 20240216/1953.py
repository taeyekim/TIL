# 1953. [모의 SW 역량테스트] 탈주범 검거

# 15125. 5105 미로의 거리

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

def bfs(stR, stC, time):
    Q = []
    visited = [[0] * N for _ in range(N)]

    Q.append((stR, stC))
    visited[stR][stC] = 1
    d = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
    pipe = {
        1: [d['up'], d['down'], d['left'], d['right']],
        2: [d['up'], d['down']],
        3: [d['left'], d['right']],
        4: [d['up'], d['right']],
        5: [d['down'], d['right']],
        6: [d['down'], d['left']],
        7: [d['up'], d['left']]
    }
    while time:

        vR, vC = Q.pop(0)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            wR = vR + dr
            wC = vC + dc

            if 0 <= wR < N and 0 <= wC < N:
                if arr[wR][wC] == 3:
                    return visited[vR][vC] # 1 or True

                if arr[wR][wC] == 0 and not visited[wR][wC]:
                    Q.append((wR, wC))
                    visited[wR][wC] = 1 # True
    return 0

T = int(input())

for tc in range(1, T+1):
    # N = 세로, M = 가로, R = 맨홀 세로, C = 맨홀 가로, 탈출 소요 시간
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)] # 세로 크기 만큼 배열 받음

    stR, stC, time = R, C, L

    print(f"#{tc} {bfs(stR, stC, time)}")

