T = int(input())

for num in range(T): 
    K, N, M = map(int, input().split()) # K = 충전 한 번당 이동 가능 거리, N = 정류장 수, M = 중전기 갯수
    arr = list(map(int, input().split())) # 충전기가 설치된 정류장 번호 1, 3, 5, 7, 9

    if arr[0] != 0: # 
        arr.insert(0, 0)
    if arr[-1] != N:
        arr.append(N)
    # arr = 0, 1, 3, 5, 7, 9, 10 이동횟수 cnt 거친 정류장 수는 cnt - 1
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