# 선생님 Stack
def push(c):
    global top
    if is_full():
        print('full-')
        return
    top += 1
    STACK[top] = c

def pop():
    global top
    if is_empty():
        print('empty-')
        return
    top -= 1
    return STACK.pop(STACK[top+1]) #앞에 데이터를 받는 것이기 때문에

def peek():
    return STACK[top]

def is_empty():
    global top
    if top < 0:
        print("empty")
        return True
    return False

def is_full():
    global top
    if top >= SIZE-1 :
        print('full')
        return True
    return False

SIZE = 10
STACK = [0] * SIZE
top = -1
print(STACK, top)
push('A')
print(STACK, top)
push('B')
print(STACK, top)
push('C')
print(STACK, top)
c = pop()
print("c:", c)
print(STACK, top)
print(pop())
print(STACK, top)
print(pop())
print(STACK, top)
print(pop())
print(STACK, top)

