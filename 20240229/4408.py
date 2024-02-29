# 4408. 자기 방으로 돌아가기

T = int(input())

for tc in range(1, T+1):
    arr = [0] * 401
    N = int(input())
    for _ in range(N):
        fr, to = map(int, input().split())
        if fr > to:
            fr, to = to, fr
        to = to + 1 if to % 2 == 1 else to
        fr = fr + 1 if fr % 2 == 1 else fr
        for i in range(fr, to+1):
            arr[i] += 1
    print(f"#{tc} {max(arr)}")