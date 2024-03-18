# # 1222. [S/W 문제해결 기본] 6일차 - 계산기1
#
s = '(6+5*(2-8)/2)'
# s = '2+3*4/5'
# '('는 무조건 push, ')' 나올 때까지 pop하면 안 됨.

def step1():

    ST = []
    result = []
    icp = {'+':1, '*':2, '-':1, '/':2, '(':100} # 토큰으로 주어진 걸 스택에 있는 기존 연산자와 비교할 때
    isp = {'+':1, '*':2, '-':1, '/':2, '(':0} # 스택에 (괄호가 있을 시에 새로 들어오는 토큰과 비교할 때

    for c in s:
        if c.isdigit():
            result.append(c)
        elif c == ')':
            while ST[-1] != '(':
                result.append(ST.pop())
            ST.pop()
        else:
            if ST and isp[ST[-1]] < icp[c]:
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:
                    result.append(ST.pop())
                ST.append(c)

    while ST:
        result.append(ST.pop())
    return result
    # print(result)

def step2(lst):
    ST = []
    for c in lst:
        if c.isdigit():
            ST.append(c)
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            # t = calc(v1, v2, c)
            ST.append(calc(v1, v2, c))
    return ST.pop()

def calc(v1, v2, op):
    if op=='+':
        return v1 + v2
    elif op=='-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 // v2

post_order = step1()
print(step2(post_order))

# operator_stack = []
# result = []
# for tc in range(1, 11):
#     N = int(input())
#     S = input()
#
#     result = []
#
#     piority = {'+' :1, '-': 1, '*':2, '/':2}
#
#     for c in S:
#         if c.isdigit():
#             result.append(c)
#         elif c == '+':
#             operator_stack.append(c)
#     while operator_stack:
#         a = result.pop()
#         b = result.pop()
#         operator_stack.pop()
#         result.append(int(a)+int(b))
#     print(f"#{tc} {result.pop()}")

