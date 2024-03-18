# 15555. 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

def merge(left, right):
    new_lst = []
    lp = 0
    rp = 0
    global cnt
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1

    # if lp < len(left):
    #     new_lst.extend(left[lp:])
    # if rp < len(right):
    #     new_lst.extend(right[rp:])
    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    if left[-1] > right[-1]:
        cnt += 1
    return new_lst

# lst의 값들을 정렬한 후 new_lst를 return
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])
    new_lst = merge(left, right)

    return new_lst

T = int(input())

for tc in range(1, 1+T):

    N = int(input())
    cnt = 0
    numbers = list(map(int, input().split()))
    sorted_lst = merge_sort(numbers)
    print(f'#{tc} {sorted_lst[N//2]} {cnt}')
