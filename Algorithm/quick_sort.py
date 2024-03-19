# s, e 사이에서 첫번째 s 위치의 값을 pivot으로
# 좌측에는 작은 값, 우측에는 큰 값들을 모으고
# pivot의 위치를 return 한다.
numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]

def partition_l(s, e):
    p = e
    i = s - 1
    for j in range(p, e-1):
        if numbers[j] < numbers[p]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

def partition_h(s, e):
    p = s
    i = s
    j = e
    # i의 위치 이동
    while i <= j:
        while i <= j and numbers[i] <= numbers[p]:
            i += 1

        # j의 위치 이동
        while i <= j and numbers[j] > numbers[p]:
            j -= 1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[p], numbers[j] = numbers[j], numbers[p]
    return p

def quick_sort(s, e):
    if s < e:

        m = partition_h(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

    # numbers [x, x, 3, x, x, x, x, x, x ...]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

N = len(numbers) - 1
quick_sort(0, N)

print(numbers)