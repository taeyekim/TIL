# 1223. [S/W 문제해결 기본] 6일차 - 계산기2


def step1(s): # 중위표기법을 후위표기법으로 변환
    ST = []
    result = []
    icp = {'+':1, '-':1, '*':2, '/':2, '(':100} # 토큰으로 주어진 걸
    isp = {'+':1, '-':1, '*':2, '/':2, '(':0}

    for c in s:
        if c.isdigit():
            result.append(c) # 토큰이 숫자일 경우 result에 표기
        elif c == ')': # 토큰이 ')'일 경우
            while ST[-1] != '(': # 스택 마지막 값이 '('가 아닐 때
                result.append(ST.pop()) # result에 ST 마지막 값을 계속 할당 '('을 만날 때까지
            ST.pop() # 스택 '(' pop
        else:
            if ST and isp[ST[-1]] < icp[c]: # 스택이 존재할 때, isp의 스택 마지막 값의 우선순위 가 토큰의 우선순위보다 낮을 때
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]: # isp 스택 마지막 값의 우선순위가 토큰의 우선순위보다 높을 때까지
                    result.append(ST.pop()) # result에 ST의 마지막값을 pop해서 더함
                ST.append(c)

    while ST:
        result.append(ST.pop())
    return result

def step2(lst):
    ST = []
    for c in lst:
        if c.isdigit():
            ST.append(c)
        else:
            v1 = int(ST.pop())
            v2 = int(ST.pop())
            t = calc(v1, v2, c)
            ST.append(t)
    return ST.pop() # ST의 마지막 계산값 반환

def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 // v2

for tc in range(1, 11):
    N = int(input())
    s = input()

    s = step1(s)
    answer = step2(s)
    print(f"#{tc} {answer}")

