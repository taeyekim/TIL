T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for x in range(0, N + 1):
        for y in range(1, N + 1):
            if x**2 + y**2 <= N**2:
                cnt += 1
    cnt = cnt * 4 + 1
    print(f"#{tc} {cnt}")