# def push(n):
#     global top
#     top += 1
#     if top == size :
#         print('overflow!')
#     else:
#         stack[top] = n
#
# top = -1
# size = 10
# stack = [0]*size # 최대 10개 push
#
# top += 1    # push(10)
# stack[top] = 10
#
# top += 1    # push(20)
# stack[top] = 20
#
# push(30)
#
# while top >= 0:
#     top -= 1
#     print(stack[top+1])

def f2(n):
    n *= 2
    print(n)
    return

def f1(c, d):
    e = c+d
    f2(e)
a = 10
b = 20
c = a + b
f1(a, b)

