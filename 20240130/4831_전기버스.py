T = int(input())

for num in range(T): 
    K, N, M = map(int, input().split()) # K = 충전 한 번당 이동 가능 거리, N = 정류장 수, M = 중전기 갯수
    arr = list(map(int, input().split()))

    if arr[0] != 0:
        arr.insert(0, 0)
    if arr[-1] != N:
        arr.append(N)

    pos = 0
    cnt = -1
    while pos != N:
        i = arr.index(pos)
        for j in range(len(arr) - 1, i, -1):
            if arr[j] - arr[i] <= K:
                pos += arr[j] - arr[i]
                cnt += 1
                break
        else:
            cnt = 0
            break
    print(f"#{num+1} {cnt}")