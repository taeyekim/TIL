# 14555. 공과 잡초

# 3
# ||||||
# (|..|)
# .|.(|...||)|...()..

T = int(input())

for tc in range(1, T+1):
    s = input()
    st = []
    cnt = 0
    for c in s:
        if c == '(':
            st.append('c')
        elif c == ')':
            if st:
                st.pop()
            cnt += 1
        elif c == '|' and st:
            st.pop()
            cnt += 1
    print(f"#{tc} {cnt}")
