# s = '(6+5*(2-8)/2)'
## s = '2+3*4/5'
##후위표기법: 연산자 우선순위에 맞도록 순서 바꿔줌
##왼쪽 괄호 무조건 푸쉬, 오른쪽 괄호 나올 때까지 계속 쌓여있어야 함

# def step1(): #operator가 스택에 들어감
#     ST = []
#     result = []
#     #연산자 우선순위 미리 만들어놓기
#     icp = {'+':1, '-':1, '*':2, '/':2, '(':100}
#     isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
#     for c in s :
#         if c.isdigit() : #c가 숫자일때
#             result.append(c) #출력하기
#         elif c == ')':
#             while ST[-1] != '(':
#                 result.append(ST.pop())
#             ST.pop() #여는 괄호 필요 없으니까 빼주기
#         else :
#             if ST and isp[ST[-1]] < icp[c] :
#                 ST.append(c)
#             else :
#                 while ST and isp[ST[-1]] >= icp[c] :
#                     result.append(ST.pop())
#                 ST.append(c) #ST 비어있으면 바로 append
#     while ST :
#         result.append(ST.pop())
#     return result
#
#
#
# def step2(lst) : #피연산자가 stack에 들어감/후위표기법은 괄호연산자까지 다 적용된 게 나옴
#     ST = [] #공유 안 하고 따로 만들어야 함
#     for c in lst :
#         if c.isdigit() :
#             ST.append(c)
#         else :
#             v2 = ST.pop()
#             v1 = ST.pop()
#             # t = calc(v1, v2, c)
#             ST.append(calc(int(v1), int(v2), c))
#     return ST.pop()
#
# def calc(v1, v2, op):
#     if op == '+':
#         return v1+v2
#     elif op == '-':
#         return v1-v2
#     elif op == '*':
#         return v1*v2
#     else :
#         return v1//v2 #정수로만 처리하기 위해(실수로 처리하면 값이 애매할 수 있음)
#
# post_order = step1()
# step2(post_order)

## s = '2+3*4/5'
## #후위표기법: 연산자 우선순위에 맞도록 순서 바꿔줌
##
## ST = []
## result = []
## #연산자 우선순위 미리 만들어놓기
## prio = {'+':1, '-':1, '*':2, '/':2}
## for c in s :
##     if c.isdigit() : #c가 숫자일때
##         result.append(c)
##     else :
##         if ST and prio[ST[-1]] < prio[c] :
##             ST.append(c)
##         else :
##             while ST and prio[ST[-1]] >= prio[c] :
##                 result.append(ST.pop())
##             ST.append(c) #ST 비어있으면 바로 append
## while ST :
##     result.append(ST.pop())
## print(result)



#<백트래킹>_부분집합
N = 10
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = [0,0,0,0] => {}
# ...
# result = [0,0,1,1] => {7,12}
# result = [1,1,1,1] => {11,3,7,12} #부분집합개수 2^N

#result = [-1]*N
# for i0 in [0,1]: #값으로 가져감
#     result[0] = i0
#     for i1 in [0,1]:
#         result[1] = i1
#         for i2 in [0,1] :
#             result[2] = i2
#             for i3 in [0,1] :
#                 result[3] = i3
#                 print(result)

# result = [-1]*N
# def subset(k): #k = 0,1,2,3,...노드
#     if k == N : #N이상으로 내려가면 안 됨
#         print(result, '=>', end='') #부분집합 사용해 계산하려면 여기서 처리
#         sumV = 0
#         for i in range(N):
#             if result[i]:
#                 sumV += numbers[i]
#         print(sumV)
#         return
#     for i in [0,1]:
#         result[k] = i
#         subset(k+1) #두번만 호출하면 됨
# subset(0)


# result = [-1]*N
# def subset(k, subSum): #k = 0,1,2,3,...노드
#     if subSum > 10 : #백트래킹
#         return
#
#     if k == N :
#         if subSum == 10 :
#             print(result, subSum)
#         return
#
#     for i in [0,1]:
#         result[k] = i
#         if i == 0 :
#             subset(k+1, subSum)
#         else :
#             subset(k + 1, subSum+numbers[k])
#
# subset(0,0)




#<중복조합>
# N = 3
# result = [-1]*N
# numbers= [23,42,15]
# #c 배열에 후보를 만들어서 갯수를 return
# def construct_candidates(k,c): #나부터 만들어서 3개/내가v일때 나를 기준으로 하려면 +v
#     c[0]=0
#     c[1]=1
#     return 2
#
# def process_solution():
#     print(result)
#     for i in range(N) :
#         if result[i] :
#             print(numbers[i], end = ' ')
#     print()
#
#
# def recur_g(k): #k는 인덱스 번호
#     if k == N : #N전까진 다 봐야함, N-1째의 값이 N에서 나오기 때문
#         process_solution()
#         return
#     c= [-1]*100
#     nC = construct_candidates(k,c) #k의 후보 만들어줘
#     for i in range(nC) : #반복문은 옆의 가지들
#         result[k] = c[i]
#         recur_g(k+1) #호출하는 아래 덱스, 재귀호출
#
# recur_g(0)

################################################################################################
N = 10
result = [-1]*N
numbers= [0,1,2,3,4,5,6,7,8,9]
def subSum(k,curS):
    if curS > 10:
        return

    if k== N: #부분집합 하나 만들어짐
        if curS == 10:
            print(result)
            for i in range(N):
                if result[i]:
                    print(numbers[i],end= ' ')
            print()
        return

        # sumV = 0
        # for i in range(N) :
        #     if result[i] :
        #         sumV += numbers[i]
        # if sumV == 10 :
        #     print(result)
        #     for i in range(N):
        #         if result[i]:
        #             print(numbers[i],end= ' ')
        #     print()
        #return

    for d in [0, 1]:
        result[k] = d
        if d == 0 :
            subSum(k + 1, curS)
        else:
            subSum(k+1, curS+numbers[k])
subSum(0, 0)

#그림 그려놓고 옆으로 가는 건 반복, 아래로 가는 건 재귀호출 k+1,
#무한으로 돌지 않게 K가 N일때 해주기