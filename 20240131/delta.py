di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
arr = [[0]*N for _ in range(N)]
i = 3
j = 4
for i in range(N):
    for j in range(N):
        for k in range(4): 
            ni = i + di[k]

            for di, dj in [[0,1], [1,0], [0,-1], [-1, 0]]
                ni nj = i+di, j+dj
            if 0 <- ni < N and 0 <= nj < N:
                print(arr[ni][nj], end = ' ')
        print(arr[])

