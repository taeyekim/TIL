# # DATA = [0, 4, 1(1), 3, 1(2), 2, 4, 1(3)]
# # TEMP = [0, 1(1), 1(2), 1(3), 2, 3, 4, 4]
# N = len(DATA)
# TEMP = [-1, -1, -1, -1, -1, -1, -1, -1]
# DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# # DATA[7] => DATA[N-1]
# TEMP = [-1, -1, -1, 1, -1, -1, -1, -1]
# COUNTS = [1, 3, 5, 6, 8]
# # DATA[6] => DATA[N-2] => 4
# TEMP = [-1, -1, -1, 1, -1, -1, -1, 4]
# COUNTS = [1, 3, 5, 6, 7]
# # DATA[5] => DATA[N-3] => 2
# TEMP = [-1, -1, -1, 1, 2, -1, -1, 4]



# DATA
# COUNTS = [1, 3, 1, 1, 2]
# COUNTS = [1, 4, 5, 6, 8] 누적합
#           0, 1, 2, 3, 4
# COUNTS = {'0':1, '1':3, '2':1, '3':1, '4':2}
DATA = [0, 4, 1, 3, 1, 2, 4, 1]
K = 4+1 # DATA에 있는 것 중 가장 큰 값 + 1 (4로 설정해도 상관없음)
N = len(DATA)
COUNTS = [0] * (K)
for d in DATA:
    COUNTS[d] += 1

for i in range(1, K):
    COUNTS[i] = COUNTS[i] + COUNTS[i-1]

# print(COUNTS)
TEMP = [-1] * N
# for d in DATA[::-1]:
for i in range(N-1, -1, -1):
    # d = DATA[i]
    # idx = COUNTS[d] - 1
    # TEMP[idx] = d
    # COUNTS[d] -= 1

    d = DATA[i]
    COUNTS[d] -= 1
    TEMP[COUNTS[DATA[i]]] = d


print(TEMP)