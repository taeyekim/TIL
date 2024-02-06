# 5432. 쇠막대기 자르기

T = int(input())

for tc in range(1, T+1):
    A = input()
    A = A.replace("()", "_")
    print(A)