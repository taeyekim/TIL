T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [0 for _ in range(N)]
    for i in range(N):
        input_arr = list(map(int,input().split()))
        arr[i] = input_arr

    kill_fly = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += arr[i+k][j+l]
            if total > kill_fly:
                kill_fly = total
    print(f"#{tc+1} {kill_fly}")