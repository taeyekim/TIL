# 4613. 러시아 국기 같은 깃발

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    LST = [input() for _ in range(N)]
    
    COUNT = [[0,0,0] for _ in range(N)]
    for i in range(N):
        COUNT[i][0] = LST[i].count('W')
        COUNT[i][1] = LST[i].count('B')
        COUNT[i][2] = LST[i].count('R')
    min_v = M*N
    for li1 in range(0, N-2):
        for li2 in range(li1+1, N-1):
            total = 0
            for i in range(0, li1+1):
                total += COUNT[i][1] + COUNT[i][2]
            for i in range(li1+1, li2 + 1):
                total += COUNT[i][0] + COUNT[i][2]
            for i in range(li2+1, N):
                total += COUNT[i][0] + COUNT[i][1]
            min_v = min(min_v, total)
    print(f"#{tc} {min_v}")