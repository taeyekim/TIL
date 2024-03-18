# 15030. 4873 반복문자 지우기

T = int(input())

for tc in range(1, T+1):
    cnt = 0
    N = list(input().strip())
    i = 0
    stack = []
    for s in N:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)

    print(f"#{tc} {len(stack)}")

