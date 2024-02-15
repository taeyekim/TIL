# 15124. 5097 회전

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))

    idx = M % N
    print(f"#{tc} {arr[idx]}")