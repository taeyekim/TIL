# 14939. 4864 문자열 비교
T = int(input())
for t in range(T):
    a = input()
    b = input()
    c = 1 if a in b else 0
    print(f"#{t+1} {c}")