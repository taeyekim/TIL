# 10804. 문자열의 거울상

T = int(input())

for tc in range(1, T+1):
    S = input()
    answer = ''
    S = S[-1::-1]
    
    
    dic = {'q' : 'p', 'p' : 'q', 'b' : 'd', 'd': 'b'}
    answer = ''
    for s in S:
        answer += dic[s]
    print(f"#{tc} {answer}")