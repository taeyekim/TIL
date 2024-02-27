# for i in range(1, 4) :
#     for j in range(1, 4) :
#         for k in range(1, 4) :
#             for r in range(1, 4) :
#                 result = str(i)+str(j)+str(k)+str(r)
#                 print(result)

# def depth(x):
#     if x == 6 :
#         return
#     print(x, end=' ')
#     depth(x+1)
#     print(x, end=' ')
#
# depth(0)

# def Tree(x) :
#     if x == 3:
#         return
#     # Tree(x+1)
#     # Tree(x+1)
#     for i in range(2):
#        Tree(x+1)
#
# Tree(0)

#순열 : 중복 안 되는 거
# path= []
#
# def KFC(x):
#     if x == 2 :
#         print(path)
#         return
#
#     for i in range(3) :
#         path.append(i)
#         KFC(x+1)
#
# KFC(0)

# 중복순열_path
# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x + 1)
#         path.pop() #리턴되면서 제거됨
#
# KFC(0)


# 순열_path,used
# path = []
# used = [False]*6 #branch만큼
#
# def KFC(x) :
#     if x == 3 :
#         print(path)
#         return
#
#     for i in range(1,7) :
#         if used[i] == True :
#             continue
#         used[i] = True
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#         used[i] = False
# KFC(0)

# 도전 문제
# def type1(x) : #중복순열
#     if x == N :
#         print(path)
#         return
#
#     for i in range(1,7):
#         path.append(i)
#         type1(x+1)
#         path.pop()
#
#
# def type2(x) : #순열
#     if x == N :
#         print(path)
#         return
#
#     for i in range(1,7):
#         if used[i] :
#             continue
#         used[i] = True
#         path.append(i)
#         type2(x+1)
#         path.pop()
#         used[i] = False
#
#
# N, type = map(int, input().split())
# path = []
# used = [False]*7 #branch만큼 초기화
#
# if type == 1 :
#     type1(0)
# else :
#     type2(0)


# #주사위 누적합 구하기
# path = []
# cnt = 0
#
# def type1(x,sum) : #중복순열
#     global cnt
#     if sum > 10 : #가지치기
#         return
#
#     if x == 3 :
#         cnt += 1
#         return
#
#     # if x == 3 :
#     #     print(f'{path} = {sum}')
#     #     return
#
#     # if x == 3 : #비효율적
#     #     if sum <= 10 :
#     #         print(f'{path} = {sum}')
#     #     return
#
#     for i in range(1,7):
#         path.append(i)
#         type1(x+i, sum+i)
#         path.pop()
#
# type1(0,0)
# print(cnt)
#-----------------------------
# path = []
#
# def KFC(x):
#
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
# KFC(0)
# ------------------------
# path = []
# used = [False] * 5
#
# lev = 3

# def KFC(x):
#
#     if x == lev:
#         print(path)
#         return
#
#     for i in range(5):
#         if used[i] == True:
#             continue
#         used[i] = True
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
#         used[i] = False
#
# KFC(0)
lev = 3
branch = 5
path = []
used = [False] * branch

def Permutation(x):
    if x == lev:
        print(path)
        return

    for i in range(branch):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        Permutation(x+1)
        path.pop()
        used[i]=False

Permutation(0)