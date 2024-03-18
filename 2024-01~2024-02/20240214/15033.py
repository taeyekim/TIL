# 15033. 4880 토너먼트 카드게임

def getWinner(w1, w2):


    return w1 ... w2


# i ~ j 중 위너의 위치를 return
def game(i, j):
    if i == j:
        return i

    winner1 = game(i, (i+j)//2)
    winner2 = game((i+j)//2 + 1, j)
    return getWinner(winner1, winner2)

N = 4
s = [1, 3, 2, 1]
game(0, N-1)

