# 5789. 현주의 상자 바꾸기

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0 for _ in range(N+1)]
    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            arr[j] = i
    print(f"#{tc} ", end = '')
    for i in range(1, N+1):
        print(f"{arr[i]} ", end = '')
    print()