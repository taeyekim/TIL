T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # 전체 페이지, A가 찾을 쪽, B가 찾을 쪽
    l = 1
    r = P
    c = (l+r)//2

    b_cnt = 0
    a_cnt = 0
    while c != Pa: # A,B각자 이진탐색으로 찾은 수가 A가 찾을 쪽 일치할 때
        if 1 <= Pa < c:
            r = c
        elif c < Pa <= r:
            l = c
        c = (l + r) // 2
        a_cnt += 1

    l = 1
    r = P
    c = (l + r) // 2
    while c != Pb:
        if 1 <= Pb < c:
            r = c
        elif c < Pb <= r:
            l = c
        c = (l + r) // 2
        b_cnt += 1

    answer = 0
    if a_cnt < b_cnt:
        answer = 'A'
    elif a_cnt > b_cnt:
        answer = 'B'

    print(f"#{tc} {answer}")