# 15561. 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

# s, e 사이에서 첫번째 s 위치의 값을 pivot으로
# 좌측에는 작은 값, 우측에는 큰 값들을 모으고
# pivot의 위치를 return 한다.
def partition_h(s, e):
    p = s
    i = s + 1
    j = e
    # i의 위치 이동
    while i <= j:
        while i <= j and A[i] <= A[p]:
            i += 1

        # j의 위치 이동
        while i <= j and A[j] >= A[p]:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]
    A[p], A[j] = A[j], A[p]
    return j

def quick_sort(s, e):
    if s < e:

        m = partition_h(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

    # A [x, x, 3, x, x, x, x, x, x ...]


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, len(A) - 1)
    print(f"#{tc} {A[N//2]}")

