'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''
T = int(input())
for tc in range(T):
    N = int(input())
    # arr= [list(map(int, input().split())) for _ in range(N)]
    newArr = [[0] * N for _ in range(N)]

    value = 0
    row = 0
    col = 0

    # 방향 중요 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    # r += dr[d]
    # c += dc[d]
    # value보다 큰 것 중 제일 작은 값을 찾아서 return
    # def getMin(value):
    #     minV = 1e10
    #     for r in range(N):
    #         for c in range(N):
    #             if value < arr[r][c] < minV:
    #                 minV = arr[r][c]
    #     return minV

    for i in range(1, N*N+1):
        newArr[row][col] = i
        newR = row + dr[d]
        newC = col + dc[d]
        if (newR >= N or newR < 0 or newC >= N or newC < 0) or newArr[newR][newC]:
            d = (d+1) % 4
        row += dr[d]
        col += dc[d]

    # print(newArr)
    print(f"#{tc+1}")
    for row in range(N):
        for col in range(N):
            print(newArr[row][col], end=' ')
        print()
        