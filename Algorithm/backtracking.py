#[백트래킹]
#완전탐색 + 가지치기
#가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 방법

#중복된 순열
#1~3까지 숫자 배열이 있을 때

#재귀함수 => 특정 시점으로 돌아오는 게 핵심!
#재귀 함수 팁
#파라미터 : 바로 작성X
#구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다!



# #재귀 전 기본 코드
# def dfs(level):
#     #기저조건
#     #이 문제에서는 3개를 뽑았을 때 까지 반복
#     if level == 3 :
#         print(*path)
#         return
#
#     #들어가기 전
#     #다음 재귀 호출
#     # - 다음에 갈 수 있는 곳들은 어디인가?
#     # - 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재
#
#     path[level] = 1
#     dfs(level+1)
#
#     path[level] = 2
#     dfs(level + 1)
#
#     path[level] = 3
#     dfs(level + 1)
#
# arr = [i for i in range(1, 4)]
# path = [0]*3
# dfs(0)
#




# #재귀 버전
# def dfs(level):
#     # 기저조건
#     # 이 문제에서는 3개를 뽑았을 때 까지 반복
#     if level == 3:
#         print(*path)
#         return
#
#     # 들어가기 전
#     # 다음 재귀 호출
#     # - 다음에 갈 수 있는 곳들은 어디인가?
#     # - 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재
#
#     # path[level] = arr[0]
#     # dfs(level + 1)
#     #
#     # path[level] = arr[1]
#     # dfs(level + 1)
#     #
#     # path[level] = arr[2]
#     # dfs(level + 1)
#
#     for i in range(len(arr)) :
#         path[level] = arr[i]
#
#
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# dfs(0)




#순열
#123,132,213,231,312,321
#시뮬레이션 돌려보고 조건 도출하거나 문제에서 조건을 바로 주는 경우 있음(잘 파악해야함)
#조건 : 숫자는 한 번만 사용해라!
# arr = [i for i in range(1, 4)]
# path = [0] * 3
#
# def dfs(level):
#     if level == 3:
#         print(*path)
#         return
#
#     #갈 수 있는 후보군
#     for i in range(len(arr)) :
#         #여기는 못 가!(가지치기)
#         #백트래킹 코드 팁
#         #갈 수 없는 경우 활용
#         #아래 코드처럼 갈 수 없을 때 continue
#
#         # if arr[i] not in path:
#         #     path[level] = arr[i]
#         #     def(level+1)
#
#         if arr[i] in path :
#             continue
#
#         path[level] = arr[i]
#         dfs(level+1)
#
#         #갔다와서 할 로직
#         #기존 방문 초기화
#         path[level] = 0
#
# dfs(0)

#백트래킹
#1. 완전 탐색 경우의 수
#2. 가지치기, 대략적인 감소 예측
#시간 초과 나면 기저조건, 가지치기 더 없는지 고민해야함
