# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
T = 10
for _ in range(T):
    tc = int(input())
    queue = list(map(int, input().split()))

    while queue[-1] != 0:
        for i in range(1, 6):
            num = queue.pop(0)
            num -= i
            queue.append(num)
            if queue[-1] <= 0:
                queue[-1] = 0
                break

    print(f"#{tc} ", end = '')
    print(*queue)
