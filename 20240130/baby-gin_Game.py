# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라

strr = input()
arr = [0 for i in range(10)]
triplet = 0
run = 0

for s in strr:
    arr[int(s)] += 1

for i in range(len(arr)):
    triplet = 0
    run = 0
    if arr[i] >= 3:
        arr[i] -= 3
        triplet += 1
        for j in range(len(arr)-2):
            if arr[j] == arr[j+1] == arr[j+2] == 1:
                run += 1
                break
    if triplet == run == 1:
        print("babi-gin")
        break
else:
    print("X")