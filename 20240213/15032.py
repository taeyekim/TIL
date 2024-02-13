# DFS - 깊이 우선 탐색 : 한번씩 가보기

N = 5
s = '1 2 1 3 3 4 4 5 4 2'
lst = list(map(int, s.split()))
G = [[] for _ in range(N+1)]

def dfs(stR, stC):
    ST = []
    visited = [[False] * N for _ in range]

    ST.append((stR, stC))
    visited[stR][stC] = True
    while ST:
        vR, vC = ST.pop()
        print(v)


        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR =
            newC =
            if 갈 수 있는 곳인지 and not visited[newR][newC]:
                골인지 아닌지 확인하는 것 (pop하면 된다는느낌)                ST.append((newR, newC))
                visited[newR][newC] =True
                if v==Goal:
                    return 1
                ST.append(v)
                visited[v] = True
    return 0

stR =
stC =
dfs(stR, stC)

