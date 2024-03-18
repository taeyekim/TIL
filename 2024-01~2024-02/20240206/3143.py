# 3143. 가장 빠른 문자열 타이핑

T = int(input())

for tc in range(1, T+1):
    A, B = input().split() # banana bana
    total = 0
    j = 0
    for i in range(len(A)):
        if A[i] == B[j]:
            j += 1
            if j == len(B):
                j = 0
                total += 1
        else:
            j = 0

    print(f"#{tc} {len(A) - total * len(B) + total}")

# T = int(input())
#
# for tc in range(1, T+1):
#     A, B = input().split() # banana bana
#     A.replace(B, '_')
#     print(f"#{tc} {len(A)}")

