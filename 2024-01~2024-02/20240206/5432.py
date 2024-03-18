# 5432. 쇠막대기 자르기

T = int(input())

for tc in range(1, T+1):
    S = input()
    stack = []
    cnt = 0
    total = 0
    S = S.replace("()", '_')
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == '_':
            cnt += len(stack)
        elif s == ')':
            stack.pop()
            cnt += 1
    print(f"#{tc} {cnt}")