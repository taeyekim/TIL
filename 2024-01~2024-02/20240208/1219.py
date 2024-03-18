# 1219. [S/W 문제해결 기본] 4일차 - 길찾기

def solve():
    ST = []
    visited = [False for _ in range(101)]
    ST.append(0)
    visited[0] = True
    
    while ST:
        v = ST.pop()
        
        for w in G[v]:
            if visited[w] == False:
                if w == 99:
                    return 1
                visited[w] = True
                ST.append(w)
    return 0
        
for tc in range(1, 11):
    T, g = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].append(v2)
    print(f"#{tc} {solve()}")