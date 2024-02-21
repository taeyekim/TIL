# 4613. 러시아 국기 같은 깃발

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ARR =

    COUNT = [[0,0,0] for _ in range(N)]
    for row in range(N):
        COUNT[row][0] = ARR[row].count('W')
        COUNT[row][1] = ARR[row].count('B')
        COUNT[row][2] = ARR[row].count('R')

    for li in range(0, N-2):
        for l2 in range(li+1, N-1):
            # print(l1, l2)
            # 0~l1까지 흰색
            # l1~l2까지 파란색
            # l2~N-1 까지 빨간색

