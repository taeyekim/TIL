# # 15388. 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
#
# def check(lst):
#     run = 0
#     triplet = 0
#     idx = 0
#     for i in range(len(lst) - 2):
#         if lst[i] == lst[i + 1] == lst[i + 2]:
#             idx = i+2
#         elif (lst[i] == lst[i+1] + 1 == lst[i+2] + 2) or (lst[i] == lst[i+1] + -1 == lst[i+2] - 2):
#             idx = i+2
#     return idx
#
# T = int(input())
#
# for tc in range(1, T+1):
#     card_list = list(map(int, input().split()))
#     player_one, player_two = [], []
#     p1_dict, p2_dict = {}, {}
#     for i in range(0, len(card_list), 2):
#         player_one.append(card_list[i])
#         player_two.append(card_list[i+1])
#     print(player_one)
#     print(player_two)
#
#     p1_idx = check(player_one)
#     p2_idx = check(player_two)
#
#     print(p1_idx, p2_idx)

def check(lst):
    run = 0
    triplet = 0
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            run = 1
        elif (lst[i] == lst[i+1] + 1 == lst[i+2] + 2) or (lst[i] == lst[i+1] + -1 == lst[i+2] - 2):
            triplet = 1
    if run == 1 or triplet == 1:
        return True
    else:
        return False

def KFC(x, lst):

    if x == 3:
        if check(path):
            answer.append(path)
            print(path)
        return

    for i in range(6):
        if used[i] == True:
            continue
        used[i] = True
        path.append(lst[i])
        KFC(x + 1, lst)
        path.pop()
        used[i] = False

T = int(input())

for tc in range(1, T+1):
    card_list = list(map(int, input().split()))
    p1, p2 = [], []
    for i in range(0, len(card_list), 2):
        p1.append(card_list[i])
        p2.append(card_list[i+1])
    print("p1:", p1)
    print("p2:", p2)

    path = []
    used = [False] * 6
    lev = 3
    answer = []

    KFC(0, p1)
    p1_check = ["p1"] + answer
    KFC(0, p2)
    p2_check = ["p2"] + answer
    print(p1_check, p2_check)