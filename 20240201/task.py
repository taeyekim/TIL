# lst에서 key를 찾아 인덱스를 return
# 못찾으면 -1을 return
# def search(lst, N, key):
#     for idx in range(N):
#         # value = lst[idx]
#         if lst[idx] == key:
#             return idx
#     return -1

# def search(lst, N, key):
#     idx = 0
#     while idx < N:
#         # value = lst[idx]
#         if lst[idx] == key:
#             return idx
#         idx += 1
#     return -1

# def search(lst, N, key):
#     idx = 0
#     while idx < N and lst[idx] != key: # 범위 비교 먼저, 값 비교는 두번째
#         idx += 1
#     if idx == N:
#         return -1
#     else:
#         return idx

# def binSearch(lst, N, key):
#     s = 0
#     e = N-1
#     while s<=e:
#         m = (s + e) // 2
#         if lst[m] == key:
#             return m
#         if lst[m] < key:
#             s = m + 1
#         else:
#             e = m-1
#     return -1

# # numbers = [4, 9, 11, 23, 2, 19, 7]
# # N = len(numbers)
# # print(search(numbers, N, 4))
# # print(search(numbers, N, 7))
# # print(search(numbers, N, 9))
# # print(search(numbers, N, 100))

# numbers = [2, 4, 7, 9, 11, 19, 23]
# N = len(numbers)
# print(binSearch(numbers, N, 4))

# numbers의 데이터를 정렬 한 후 정렬 결과를 리스트로 return
def selectionS(numbers):
    N = len(numbers)
    # phase = 0 # 0에서 N-1 중 제일 작은 값의 위치를 찾아서 0번째와 교환
    # phase = 1 # 1에서 N-1 중 제일 작은 값의 위치를 찾아서 1번째와 교환
    # phase = 2 # 1에서 N-1 중 제일 작은 값의 위치를 찾아서 2번째와 교환
    # n = 5 하면 phase 3
    for phase in range(N - 1):
        # minV = numbers[phase]
        minP = phase
        for idx in range(phase + 1, N):
            if numbers[minP] > numbers[idx]:
                # minV = numbers[minP]
                minP = idx
        numbers[minP], numbers[phase] = numbers[phase], numbers[minP]
    return numbers

numbers = [64, 25, 10, 22, 11]
print(selectionS(numbers))
print(selectionS([64, 25, 10, 22, 11, -2]))