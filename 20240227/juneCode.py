def minsum(row, col, s):
    global minS

    # 백트래킹
    if minS <= s:
        return

    if row == N-1 and col == N-1:
        if minS > s:
            minS = s
        return
    else:
        for i in range(2):
            newR = row + ni[i]
            newC = col + nj[i]
            if newR < N and newC < N:
                minsum(newR, newC, s + arr[newR][newC])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ni = [1, 0]
    nj = [0, 1]

    minS = 10 * N
    minsum(0, 0, arr[0][0])

    print(f'#{tc} {minS}')