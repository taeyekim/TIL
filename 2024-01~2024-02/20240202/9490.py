# 9490. 풍선팡

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            
            for k in range(4):
                ni = i
                nj = j
                cnt = arr[i][j]
                while cnt:
                    ni += di[k]
                    nj += dj[k]
                    if 0 <= ni <= N-1 and 0 <= nj <= M-1:
                        total += arr[ni][nj]
                    else:
                        break
                    cnt -= 1
                    
            if max_cnt < total:
                max_cnt = total
    print(f"#{tc} {max_cnt}")