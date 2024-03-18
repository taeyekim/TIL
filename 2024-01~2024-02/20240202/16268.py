# 16268. 풍선팡2

T = int(input())
di = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for i in range(N):
        for j in range(M):
            
            total = arr[i][j]
            
            for k in range(4):
                ni = i + di[k]
                ny = j + dy[k]
                if 0 <= ni <= N-1 and 0 <= ny <= M-1:
                    total += arr[ni][ny]
            if max_num < total:
                max_num = total
    
    print(f"#{tc} {max_num}")