# 15181. 5178 노드의 합

def postOrder(root):
    # if root <= N and TREE[root]:
    #     return TREE[root]
    # v = 0

    if root * 2 <= N:
        TREE[root] += postOrder(root*2)
    if root * 2 + 1 <= N:
        TREE[root] += postOrder(root * 2 + 1)

    return TREE[root]
    # TREE[root] = v1 + v2
    # return TREE[root]
    # TREE[root] = TREE[root * 2] + TREE[root * 2 + 1]

T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split())
    TREE = [0] * (N+1)
    for _ in range(M):
        no, value = map(int, input().split())
        TREE[no] = value

    print(f'#{tc} {postOrder(L)}')

