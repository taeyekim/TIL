def make(p):
    print(len(jump), jump)
    M = len(p)
    for i in range(M):
        c = p[i]
        jump[ord(c)] = M-1-i
    print(jump[ord('m')])
    print(jump[ord('r')])

def find(p, t):
    M = len(p)
    N = len(t)

    ti = 0
    pi = M-1

    while ti+pi< N and pi>=0: #ti+pi되어야 좌표가 됨
        if t[ti+pi] == p[pi]:
            pi -= 1
        else:
            pos = ord(t[ti+pi])
            ti += jump[pos]  #ti가 시작위치이기에 점프할 수치를 찾아온 것임
            pi = M-1

    if pi<0:
        return ti
    else:
        return -1

t = 'a pattern matching algorithm'
p = 'rithm'

jump = [len(p)] * (ord('z') + 1)
make(p)