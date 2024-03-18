# 연속한 1의 갯수

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    strn = input()
    max_cnt = 0
    cnt = 0
    for s in strn:
        if s == '0':
            cnt = 0
        elif s == '1':
            cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")