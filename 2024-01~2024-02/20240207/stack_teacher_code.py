# 선생님 Stack
# def push(c):
#     global top
#     if is_full():
#         print('full-')
#         return
#     top += 1
#     STACK[top] = c
#
# def pop():
#     global top
#     if is_empty():
#         print('empty-')
#         return
#     top -= 1
#     return STACK[top+1] #앞에 데이터를 받는 것이기 때문에
#
# def peek():
#     return STACK[top]
#
# def is_empty():
#     if pop < 0:
#         print("empty")
#         return True
#     return False
#
# def is_full():
#     if top >= SIZE-1 :
#         print('full')
#         return True
#     return False
#
# SIZE = 10
# STACK = [0] * SIZE
# top = -1
# push('A')
# push('B')
# push('C')
# c = pop()
# print(c)
# print(pop())
# print(pop())
# print(pop())

# 연습문제2 - 괄호의 짝을 검사하는 프로그램
s = '( )( )((( )))'
s = '((( )((((( )( (((( )( ))((( ))))))'

# stack = []
# for c in s:
#     if c == '(':
#         STACK.append(C)
#     elif c == ')':
#         if len(STACK) > 0 and STACK.pop() == '(':
#             temp = STACK.pop()
#             if temp == '(':
#                 continue
#         else:
#             retult = False
#             break
# if len(STACK)) > 0
#     result = FALSE
#

def fun2(x):
    x *= 2
    print("func2=>", x)

def fun2(x):
    x +=1
    print("func2=>", x)

for i in range(1, 5):
    print('main=>', i)
    fun1(i)