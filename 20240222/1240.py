# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = ['0001101', '0011001', '0010011', '0111101',
           '0100011', '0110001', '0101111', '0111011',
           '0110111', '0001011']
    x, y = 0, 0
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                x = i
                y = j
    y -= 55
    s_lst = []
    for _ in range(8):
        s = arr[x][y:y+7]
        s_lst.append(s)
        y += 7
    answer = ''
    for s in s_lst:
        answer += str(lst.index(s))
    total = 0
    sum = 0
    for i in range(len(answer)):
        if i % 2 == 1:
            total += int(answer[i])
        else:
            total += int(answer[i]) * 3
        sum += int(answer[i])
    if total % 10 != 0:
        sum = 0
    print(f"#{tc} {sum}")