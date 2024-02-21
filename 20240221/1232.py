# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산

def calculator(a, b, operator):
    op = ['+', '-', '*', '/']

    if operator == op[0]:
        return a + b
    elif operator == op[1]:
        return a - b
    elif operator == op[2]:
        return a * b
    else:
        return a / b

def postOrder(root):
    # if root <= N and TREE[root]:
    #     return TREE[root]
    # v = 0

    if TREE[root][0] in ['+', '-', '*', '/']:
        v1 = float(postOrder(int(TREE[root][1])))
        v2 = float(postOrder(int(TREE[root][2])))
        value = calculator(v1, v2, TREE[root][0])
        TREE[root][0] = str(value)
        return str(value)
    else:
        return TREE[root][0]

    # if root * 2 <= N:
    #     TREE[root] += postOrder(root*2)
    # if root * 2 + 1 <= N:
    #     TREE[root] += postOrder(root * 2 + 1)
    #
    # return TREE[root]
    # TREE[root] = v1 + v2
    # return TREE[root]
    # TREE[root] = TREE[root * 2] + TREE[root * 2 + 1]

T = 10

for tc in range(1, T+1):
    N = int(input())
    TREE = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = input().split()
        no = int(lst[0])
        TREE[no] = lst[1:]
    print(f'#{tc} {postOrder(1)}')
