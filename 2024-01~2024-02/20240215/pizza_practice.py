

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))

    # print(N, M, Ci)

    pan = [0] * N # N칸 만큼의 팬
    nextPizzaNo = 1
    while pan:
        pizzaNo = pan.pop(0)
        # pizzaNo의 치즈량을 1/2로 감소
        Ci[pizzaNo] //= 2
        if Ci[pizzaNo] == 0:
            if nextPizzaNo <= M: # M개의 피자보다 nextPizzaNo가 낮으면
                pan.append(nextPizzaNo)
                nextPizzaNo += 1
        else:
            # pizzaNo를 다시 pan에 pan.append(pizzaNo)
            pan.append(pizzaNo)

    print(f"#{tc} {pizzaNo}")

