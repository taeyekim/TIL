'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# def preOrder(root):
#     print(root)
#     if leftC[root]:
#         preOrder(leftC[root])
#     if rightC[root]:
#         preOrder(rightC[root])

# def preOrder(root):
#     if root:
#         print(root)
#         preOrder(leftC[root])
#         preOrder(rightC[root])

def postOrder(root):
    if root:
        postOrder(leftC[root])

N = int(input())
lst = list(map(int, input().split()))
# TREE = [[] for _ in range(N+1)]
leftC = [0] * (N+1)
rightC = [0] * (N+1)
for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]

    if leftC[p] == 0:
        leftC[p] = c
    else:
        rightC[p] = c

print(leftC)
print(rightC)
# print(TREE)

# preOrder(1)
# postOrder(3)