 # 14941. 4865 글자수

T = int(input())

for tc in range(1, T+1):
    set1 = set(input())
    str2 = input()
    max_num = 0
    for s in set1:
        cnt = 0
        for i in range(len(str2)):
            if s == str2[i]:
                cnt += 1
        if max_num < cnt:
            max_num = cnt
    print(f"#{tc} {max_num}")