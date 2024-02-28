# 10761. 신뢰

T = int(input())

for tc in range(1, T+1):

    lst = input().split()
    N = int(lst[0]) # 로봇 이동 경우의 수(B, O 총합)
    time = 0
    pos = {'B':1, 'O':1}
    for i in range(1, len(lst) - 2, 2): # B 2 O 1 O 2 B 4
        time += 1
        robot = lst[i]
        if robot == lst[i+2]:
            if pos[robot] < lst[i+1]:
                pos[robot] += 1
            elif pos[robot] > lst[i+1]:
                pos[robot] -= 1
            else:
                continue
        else:
            if pos[robot] < lst[i + 1]:
                pos[robot] += 1
            elif pos[robot] > lst[i + 1]:
                pos[robot] -= 1
            else:
                continue

