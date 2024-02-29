def start():
    sold_bread = 0
    for person in customers:
        made_bread = (person // M) * K

        sold_bread += 1

        remain = made_bread - sold_bread

        if remain < 0:
            return 'Impossible'
    return 'Possible'


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    result = start()

    print(f'#{tc} {result}')