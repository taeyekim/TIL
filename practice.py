T = int(input())

def check():
    now = 0
    cnt = 0
    for i in range(1, M): # 1 ~ M-1
        if STOPS[i] - STOPS[i-1] > K:
            return 0

    # print(K, N, M, STOPS)
        if now+K < STOPS[i]:
            cnt += 1
            now = STOPS[i-1]
    return cnt

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K = 최대 이동 거리 / N 정류장 수 / M 충전기 개수
    STOPS = [0] + list(map(int, input().split())) +[N] # [0, 1, 3, 5, 7, 9, N]
    M += 2

    print(f'#{tc} {check()}')