# 14941. 4865 글자수

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    total = 0
    for s in set(str1):
        cnt = str2.count(s)
        total = cnt if total < cnt else total
    print(f"#{tc + 1} {total}")