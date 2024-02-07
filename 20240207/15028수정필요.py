# 15028. 4866 괄호검사

T = int(input())

for tc in range(1, T+1):
    s = list(input())
    ST = []
    pair = {'}': '{', ')': '('}
    result = 1
    for c in s:
        if c in ['(', '{']:
            ST.append(c)
        elif c in [')', '}']:
            if len(ST) == 0 or ST[-1] != pair[c]:
                result = 0
                break
    if len(ST) > 0:
        result = 0
    print(f"{tc} {result}")
