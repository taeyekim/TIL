'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# # 전위순회
# def pre_order(T):
#     if T:
#         print(T, end = ' ')
#         pre_order(left[T])
#         pre_order(right[T])
#
# N = int(input())         #1번부터 N번까지인 정점
# E = N - 1    #정점이 간선수보다 하나 더 많기 때문에 하나 뺴줘야함
# arr = list(map(int, input().split()))
# left = [0] * (N+1)       #부모를 인덱스로 왼쪽 자식 번호 저장
# right = [0] * (N+1)
# par = [0] * (N+1)        #자식을 인덱스로 부모 저장
#
# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
# # for i in range(0, N*2, 2):
# #     p, c = arr[i], arr[i+1]
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p
#
# c = N
# while par[c] != 0:    #부모가 있으면
#     c = par[c]        #부모를 새로운 자식으로 두고
# root = c              #더이상 부모가 없으면 root
# print(root)
# pre_order(root)

# # --------------------------------
# 전위순회
# def preOrder(root):
#     print(root)
#     # l = Tree[root][0]
#     # r = Tree[root][1]
#     if len(Tree[root]) >= 1:      #자식 노드가 하나 이상인 경우 (왼쪽이 있는 경우)
#         preOrder(Tree[root][0])
#     if len(Tree[root]) == 2:     #오른쪽이 있는 경우
#         preOrder(Tree[root][1])
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# Tree = [[] for _ in range(N+1)]
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx+1]  #부모와 자식은 관계가 명확하여 단방향임
#
#     Tree[p].append(c)
#     print(Tree)
#     -----------------------------------
# #  후위순회
# def postOrder(root):
#     print(root)
#     # l = Tree[root][0]
#     # r = Tree[root][1]
#     if len(Tree[root]) >= 1:      #자식 노드가 하나 이상인 경우 (왼쪽이 있는 경우)
#         postOrder(Tree[root][0])
#     if len(Tree[root]) == 2:     #오른쪽이 있는 경우
#         postOrder(Tree[root][1])
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# Tree = [[] for _ in range(N+1)]
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx+1]  #부모와 자식은 관계가 명확하여 단방향임
#
#     Tree[p].append(c)
#     print(Tree)
#
# postOrder(1)

# ---------------------------------------
# 전위순회
# def preOrder(root):
#     print(root)
#     # l = Tree[root][0]
#     # r = Tree[root][1]
#     if leftC[root]:
#         preOrder(leftC[root])
#     if rightC[root]:
#         preOrder(rightC[root])
#
#     if len(Tree[root]) >= 1:      #자식 노드가 하나 이상인 경우 (왼쪽이 있는 경우)
#         preOrder(Tree[root][0])
#     if len(Tree[root]) == 2:     #오른쪽이 있는 경우
#         preOrder(Tree[root][1])
#
# def preOrder(root):
#     if root:
#         print(root)
#         preOrder(leftC[root])
#         preOrder(rightC[root])
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# Tree = [[] for _ in range(N+1)]
# leftC = [0] * (N+1)
# rightC = [0] * (N+1)
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx+1]  #부모와 자식은 관계가 명확하여 단방향임
#
#     if leftC[p] == 0:
#         leftC[p] = c
#     else:
#         rightC[p] = c
#
# print(leftC)
# print(rightC)
#
#     # Tree[p].append(c)
#     # print(Tree)

# preOrder(1)
# -------------------------
# 전위순회

# def postOrder(root):
#     if root:
#         postOrder(leftC[root])
#         postOrder(rightC[root])
#         print(root)
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# Tree = [[] for _ in range(N+1)]
# leftC = [0] * (N+1)
# rightC = [0] * (N+1)
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx+1]  #부모와 자식은 관계가 명확하여 단방향임
#
#     if leftC[p] == 0:
#         leftC[p] = c
#     else:
#         rightC[p] = c
#
# print(leftC)
# print(rightC)
#
#     # Tree[p].append(c)
#     # print(Tree)
#
# postOrder(1)

# ----------------------------
# 후위순회
# def postOrder(root):
#     if Tree[root]:
#         postOrder(root*2)
#         postOrder(root*2+1)
#         print(root, Tree[root])
#
#
# s = 'TEST 순회! 테스트'
# lst = list(s)
# N = len(lst)
# Tree = [0] * 100
#
#
# for idx in range(N):
#     Tree[idx-1] = lst[idx]
#     # Tree[p].append(c)
# print(Tree)
#
# postOrder(1)
#
# # -------------------------------------------------
# 전위순회
def preOrder(root):
    if Tree[root]:
        print(root, Tree[root])
        preOrder(root * 2)
        preOrder(root * 2 + 1)

s = 'TEST 순회! 테스트'
lst = list(s)
N = len(lst)
Tree = [0] * 100
for idx in range(N):
    Tree[idx+1] = lst[idx]

print(Tree)
preOrder(1)