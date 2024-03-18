# N = 10
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # result = [0, 0, 0, 0] => {}
# # ...
# # result = [0, 0, 1, 1] => {7, 12}
# # result = [1, 1, 1, 1] => {11, 3, 7, 12}
# # result = [-1] * N
# # for i0 in [0, 1]:
# #     result[0] = i0
# #     for i1 in [0, 1]:
# #         result[1] = i1
# #         for i2 in [0, 1]:
# #             result[2] = i2
# #             for i3 in [0, 1]:
# #                 result[3] = i3
# #                 print(result)
#
# result = [-1] * N
# # def subset(k, subSum):
# #     if k==N:
# #         print(result, '=>', end='')
# #         sumV = 0
# #         for i in range(N):
# #             if result[i]:
# #                 sumV += numbers[i]
# #         print(sumV)
# #         return
# #
# #     for i in [0, 1]:
# #         result[k] = i
# #         subset(k+1)
#
# def subset(k, subSum):
#     if subSum > 10:
#         return
#     if k==N:
#         if subSum == 10: # process_solution(..)
#             print(result, subSum)
#         return
#     # c = [0] * 100
#     # ncandidates = construct_candidates()
#     for i in [0, 1]:
#         result[k] = i
#         if i == 0:
#             subset(k + 1, subSum)
#         else:
#             subset(k + 1, subSum+numbers[k])
#
# def construct_candidates(c):
#     c[0] = 0
#     c[1] = 1
#     return 2
#
# def subset(k):
#     if k==N:
#         process_solution(..)
#         return
#
#     c = [0] * 100
#
# subset(0, 0)
# # print(result)

#----------------

N = 3
result = [-1] * N

def construct_candidates(k, c):
    c[0] = 0
    c[1] = 1
    c[2] = 2
    return 3

def process_solution():
    print(result)
    for i in range(N):
        if result[i]:
            print(numbers[i], end = ' ')
    print()

def recur_g(k):
    if k==N:
        process_solution()
        return

    c = [-1] * 100
    nC = construct_candidates(k, c)
    for i in range(nC):
        result[k] = c[i]
        recur_g(k+1)

recur_g(0)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sumV = 0

def subSum(k):
    if k == N:
        print(result)
        sumV = 0
        for i in range(N):
            if result[i]:
                sumV += numbers[i]
        print(sumV)
        if sumV == 10:
            print(result)
            for i in range(N):
                if result[i]:
                    print(numbers[i], end = ' ')
            print()

def subSum(k, curS):
    if curS > 10:
        return

    if k==N:

        return

    for d in [0, 1]:
        result[k] = d
        if d==0:
            subSum(k + 1, curS)
        else:
            subSum(k + 1, curS + numbers[k])

Subsum(0)

