# # 순열
# def print_data(path) : #모든 값에 대해 하기 때문에 완전 탐색
#     for idx in path :
#         print(arr[idx], end=' ')
#     print()
#
# def perm(k, N, K) : #N개의 데이터로 K개의 순열을 재귀로 만들기
#     if k == K :
#         print(path)
#         print_data(path)
#         return
#
#     for i in range(N) :         #옆으로 가는 거니까 데이터 개수 넣기
#         if not visited[i] :
#             path[k] = i         #k번째에 i값 넣어주기
#             visited[i] = True
#             perm(k+1, N, K)     #중복순열
#             visited[i] = False
#
# arr = ['a','b','c','d','e']
# N = 5
# K = 3
#
# path =[-1]*K
# visited = [False]*N #사용여부니까 데이터 개수 만큼 만들기
# perm(0, N, K)



# 부분집합
# def subSum(path) :
#     sumV = 0
#     for idx in range(N) :
#         if path[idx]:
#             print(arr[idx], end =' ')
#     print()
#
#
# def subSet(k) :
#     if k == N : #원소 다 봐야함/아래로 가는 lv
#         #print(path)
#         subSum(path)
#         return
#
#     # for i in range(2) : #옆으로 가는 branch
#     #     path[k] = i
#     #     subSet(k+1) #독립적으로 만드니까 visited 안 해도 됨
#
#     path[k] = 0
#     subSet(k+1)
#
#     path[k] = 1
#     subSet(k+1)
#
# arr = ['a','b','c','d','e']
# N = 5
# K = 3
#
# path = [-1]*N
# subSet(0)

# # 조합
# def combi(k, start) :
#     global cnt
#     cnt +=1
#
#     if k == K :
#         print(path)
#         return
#
#     for i in range(start, N-K+1+k): # 마지막 [5,5] => 반복 안함
#         path[k] = i
#         combi(k+1, i+1) #i 다음부터 해줘
#     return
#
# arr = ['a','b','c','d','e']
# N = 5
# K = 3
# cnt = 0
# path = [-1]*K
# combi(0, 0)

# 그리디(회의실)
# lst = [(1,4), (3,5), (1,6), (5,7), (3,8), (5,9), (6,10), (8,11), (2,13), (12,14)]
# lst.sort(key = lambda x:x[1]) #하나하나를 x라고 한다면
# N = len(lst)
# #print(lst)
#
# # lst2 = []
# # for d in lst :
# #     d = list(d)
# #     d[0], d[1] = d[1], d[0]
# #     lst2.append(d)
# # lst2.sort()
# # print(lst2)
#
# #개수나 범위 정해져있을 때 for, 유동적이면 while
# idx = 0
# while idx < N :
#     s = lst[idx][0]
#     e = lst[idx][1]
#     print(s,e)
#     while idx < N and e > lst[idx][0] : #안 되는 경우/종료시간보다 시작시간이 빠른 경우  #건너 뛰거나 개수 셀 때 while 씀
#         idx += 1


#10761.신뢰
T = int(input())
for tc in range(1,T+1) :
    lst = input().split()

    N = int(lst[0])
    robot, x = lst[1], int(lst[2]) # 앞에 꺼 체크 안 되니까 미리 넣어두고 가자
    pre_robot = robot
    pre_time = x
    pos = {'B':1, 'O':1}           # 앞에 위치 나온 거 이어서 써야 하니까 위치 변수 잡아놓기
    pos[robot] = x
    total = x

    for i in range(3, len(lst), 2) :
        robot, x = lst[i], int(lst[i+1])
        if pre_robot == robot :
            time = abs(x-pos[robot]) +1 # 절댓값(지금 위치 - 아까 위치) 버튼 눌러야 하니까 +1
            pre_time += time            # 다음에 나타나는 애들을 위해 조정 작업(pos[robot]까지)
            # pre_robot = robot
            # pos[robot] = x
            # total += time
        else :
            time = abs(x-pos[robot]) #이동시간
            if time < pre_time: #내 이동시간이 기다리던 시간 보다 작으면/뺀 게 음수면
                time = 1
            else:
                time = time - pre_time + 1 #더 걸린 시간 구하기 + 1(버튼 누르는 시간)

            pre_time = time #???
            # pre_robot = robot
            # pos[robot] = x
            # total += time
        pre_robot = robot
        pos[robot] = x
        total += time
    print(f'#{tc} {total}')

# 3
# 4 B 2 O 1 O 2 B 4
# 3 B 5 B 8 O 100
# 2 O 2 O 1