# T = int(input())

# for tc in range(1, T+1):
#     P, Pa, Pb = map(int, input().split()) # 전체 페이지, A가 찾을 쪽, B가 찾을 쪽
#     l = 1
#     r = P
#     c = (l+r)//2

#     b_cnt = 0
#     a_cnt = 0
#     while c != Pa: # A,B각자 이진탐색으로 찾은 수가 A가 찾을 쪽 일치할 때
#         if 1 <= Pa < c:
#             r = c
#         elif c < Pa <= r:
#             l = c
#         c = (l + r) // 2
#         a_cnt += 1

#     l = 1
#     r = P
#     c = (l + r) // 2
#     while c != Pb:
#         if 1 <= Pb < c:
#             r = c
#         elif c < Pb <= r:
#             l = c
#         c = (l + r) // 2
#         b_cnt += 1

#     answer = 0
#     if a_cnt < b_cnt:
#         answer = 'A'
#     elif a_cnt > b_cnt:
#         answer = 'B'

#     print(f"#{tc} {answer}")

T = int(input())

# A의 중간 페이지 찾는 과정
# 이진 검색
def binSearch(P, key):
    S = 1 # Start
    E = P # End = 전체 페이지 할당
    i = 0 # count 횟수
    C = (1 + P) // 2
    while 1 <= C <= P: # 400(전체 페이지) 300(A가 찾을 쪽) 350(B가 찾을 쪽)
        C = (S + E) // 2 # C = 센터 중간값
        
        if C < key: # key(찾을 값)가 C(중간값)보다 큰 경우
            S = C
        elif C > key: #
            E = C
        i += 1
        
        if C == key:
            return i # i 횟수 뱉어내고 반복문 종료

for TC in range(1, T + 1):
    P, A, B = list(map(int, input().split()))

    answer = 0
    if binSearch(P,A) < binSearch(P,B) :
        answer = 'A'
    elif binSearch(P,A) > binSearch(P,B) :
        answer = 'B'
    print(f'{TC} {answer}')