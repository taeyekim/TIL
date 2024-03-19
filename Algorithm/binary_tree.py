#[트리]
#싸이클이 없는 무향 연결 그래프
# 1.싸이클: 방문했던 노드로 다시 돌아오는 다른 경로가 있는 경우
# 2.무향: 간선에 방향 없음(양방향)
# 3.연결 그래프: 모든 꼭지점이 서로 갈 수 있는 경로가 있음
# > 두 노드(or 정점) 사이에는 유일한 경로가 존재
# > 각 노드는 최대 하나의 부모 노드가 존재할 수 있음
# > 각 노드는 자식 노드가 없거나 하나 이상 존재할 수 있음
# > 형제 노드끼리는 연결 안 됨(싸이클 발생하기 때문에)
# > 최악의 경우 차수(후보군의 수)와 높이(시간 복잡도)가 몇이 나올지 생각해봐야함

#[이진트리]
#모든 노드들이 최대 2개의 서브 트리를 갖는 특별한 형태의 트리
#노드의 개수가 N개일 때, 이진 트리 높이의 h는 몇이 될까?
#최악의 경우 : 높이 h = N (편향이진트리)
#최선의 경우 : 높이 h = logN (완전이진트리)

#[포화이진트리]
#모든 레벨에 노드가 포화상태로 채워진 이진 트리

#[완전이진트리] : 가장 중요
#포화이진트리의 노드 번호 1~n번까지 빈 자리가 없는 이진 트리

#[편향이진트리]
#한쪽 방향의 자식 노드만 가진 이진 트리

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# #정석 개발 버전
# class TreeNode :
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, child):
#         #왼쪽에 삽입 시도
#         if not self.left :
#             self.left = child
#             return
#
#         #오른쪽에 삽입 시도
#         if not self.right :
#             self.right = child
#             return
#
#        #삽입 실패
#         return
#
#     def inorder(self):
#         if self != None :
#             #왼쪽이 있으면 계속 탐색
#             if self.left :
#                 self.left.inorder()
#
#             print(self.value, end=' ')
#
#             #오른쪽이 있으면 계속 탐색
#             if self.right :
#                 self.right.inorder()
#
#
#
# #이진 트리 만들기
# #1. 노드들을 생성
# nodes = [TreeNode(i) for i in range(0,14)]
#
# #2. 간선 연결
# for i in range(0, len(arr), 2) :
#     parent_node = arr[i]
#     child_node = arr[i+1]
#     nodes[parent_node].insert(nodes[child_node])
#
# nodes[1].inorder()


#코딩테스트에서는 간단하게
#키워드 : 인접리스트!
# nodes = [[] for _ in range(14)]
# for i in range(0, len(arr), 2) :
#     parent_node = arr[i]
#     child_node = arr[i+1]
#     nodes[parent_node].append(child_node)
#
# #자식이 없다는 걸 표시하기 위해 None
# for li in nodes:
#     for _ in range(len(li), 2):
#         li.append(None)
#
#
# #중위순회 구현
# def inorder(nodeNum) :
#     #갈 수 없다면 skip
#     if nodeNum == None :
#         return
#
#     #왼쪽으로 갈 수 있다면 진행
#     inorder(nodes[nodeNum][0])
#     print(nodeNum, end = ' ')
#     #오른쪽으로 갈 수 있다면 진행
#     inorder(nodes[nodeNum][1])
#
# inorder(1)


#중요! 탐색, 삽입, 삭제 시간은 트리의 높이만큼 걸림

#힙
#삽입 : 일단 마지막에 삽입 -> 자리 찾아가기
#삭제 : 루트만 삭제할 수 있으니까 max heap이면 내림차순, min heap이면 오름차순