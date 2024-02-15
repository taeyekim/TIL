# 15031. 4874 Forth

def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        return a // b

T = int(input())

for tc in range(1, T+1):
    stack = []
    arr = list(input().split())
    answer = 'error'
    for c in arr:
        if c.isdecimal():
            stack.append(c)

        elif c == '.':
            if len(stack) != 1:
                break
            answer = stack.pop()
            break
        else:
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(calc(a, b, c))
            else:
                break

    print(f"#{tc} {answer}")