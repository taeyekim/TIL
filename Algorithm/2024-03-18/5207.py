
def binarySearch_Recur(N_lst, low, high, target, direction):
    if low > high:
        return False

    mid = (low + high) // 2
    if N_lst[mid] == target:
        return True
    if N_lst[mid] < target:
        if direction == 1:
            return False
        return binarySearch_Recur(N_lst, mid + 1, high, target, 1)
    else:
        if direction == -1:
            return False
        return binarySearch_Recur(N_lst, low, mid - 1, target, -1)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_lst = sorted(list(map(int, input().split())))

    M_lst = list(map(int, input().split()))
    cnt = 0
    for s in M_lst:
        if binarySearch_Recur(N_lst, 0, N - 1, s, 0) == True:
            cnt += 1
    print(f"#{tc} {cnt}")