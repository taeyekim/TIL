# 15126. 5099 피자 굽기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))

    # print(N, M, Ci)

    pan = [0] * N
    nextPizzaNo = 1
    while pan:
        pizzaNo = pan.pop(0)
        # pizzaNo의 치즈량을 1/2로 감소
        Ci[pizzaNo] //= 2
        if Ci[pizzaNo] == 0:
            if nextPizzaNo <= M: # 남은 피자가 있으면
                pan.append(nextPizzaNo)
                nextPizzaNo += 1
        else:
            #- pizzNo 를 다시 pan에 (pan.append(pizzaNo))
            pan.append(pizzaNo)
        print(f"pan : {pan}, pizzaNo : {pizzaNo}, nextPizzaNo : {nextPizzaNo}")
    print(f'#{tc} {pizzaNo}')


