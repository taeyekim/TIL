# DFS - 깊이 우선 탐색 : 한번씩 가보기

G = [[],[2, 3],[1,3],]
def dfs(stR, stC)
    ST = []
    visited = []
    ST.append((stR, stC))
    while ST:
        vR, vC = ST.pop()
        if not visited[vR][vC]:
            visited[vR][vC] = True
            print(v)

        for dr, dc in [(), (), (), ()]:
            newR, newC
            if...
            if not visited[w]:
                ST.append(w)

def solve():
    row, col = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row, col = i, j

    ST = []
    ST.append((row, col))
    visited = [[0] * N for _ in range(N)]
    visited[row][col] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while ST:
        current_row, current_col = ST
        if arr[current_row][current_col] == 3:
            return 1
        for d in range(4):
            new_row = current_row + dr[d]
            new_col = current_col + dc[d]
            if 0 <= new_row < N and 0 <= new_col < N and arr[new_row][new_col] != 1 and not visited[new_row][new_col]:
                ST.append((new_row, new_col))
                visited[new_row][new_col] = 1
                break
        else:
             ST.pop()
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = solve()
    print(f"#{tc} {result}")
