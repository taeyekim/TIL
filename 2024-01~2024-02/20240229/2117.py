# 2117. [모의 SW 역량테스트] 홈 방범 서비스



def solve(row, col):

    # row, col에서 집까지의 거리의 갯수가 K에 저장되도록
    K = ([0] * N) * N
    for i in range(N):
        for j in range(N):
            K[i][j] += (abs(row - i) + abs(col - j))

# ====================
Home = [(2,3), (3,4), (5,6)]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    for row in range(N):
        for col in range(N):
            solve(row, col)
