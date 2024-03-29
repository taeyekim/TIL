import sys
sys.stdin = open("input.txt", "r")

# 이 문제가 왜 DP로도 해결이 가능할까?
# 1. 작은 문제로 분할할 수 있어야 한다. 작은 문제. -> 해를 저장 + 재활용
#   - 전체의 합 = 각 달까지의 최소들이 쌓여서 완성
#   - 각 달까지의 최소 비용 문제로 분할
# 2. 뒤의 결과를 구할 때, 앞에서 구했던 결과가 바뀌면 안된다.


# def dfs(month, sum_cost):
#     global ans
#
#     # 기저 조건
#     # 1. 12월까지 다 봤네? 종료
#     if month > 12:
#         # 최소 비용
#         ans = min(ans, sum_cost)
#         return
#
#     # 2. 이미 최소값을 넘어갔네? 종료
#     if sum_cost > ans:
#         return
#
#     # 모두 1일권으로 구매
#     dfs(month + 1, sum_cost + (days[month] * cost[0]))
#
#     # 1달권 구매
#     dfs(month + 1, sum_cost + cost[1])
#     # 3달권 구매
#     dfs(month + 3, sum_cost + cost[2])
#     # 1년권 구매
#     dfs(month + 12, sum_cost + cost[3])
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     # 아 인덱스 너무 머리 아파!
#     # 1부터 쓸래 (맨 앞에 0 쓰레기값 넣을래)
#     days = [0] + list(map(int, input().split()))
#     ans = int(1e9)
#     dfs(1, 0)
#     print(f"#{tc} {ans}")



T = int(input())

for tc in range(1, T + 1):
    cost = list(map(int, input().split()))
    # 아 인덱스 너무 머리 아파!
    # 1부터 쓸래 (맨 앞에 0 쓰레기값 넣을래)
    days = [0] + list(map(int, input().split()))
    # DP 배열
    plans = [0] * 13

    # 1~12월까지 반복
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        #이전 달 + 1일권 구입 / 이전 달 + 1달권 구입 / 3달 전 + 3달권 구입 그 중에서 최소
        plans[i] = min(plans[i - 1] + (days[i] * cost[0]), plans[i - 1] + cost[i])

        if i >= 3:
            plans[i] = min(plans[i], plans[i - 3] + cost[2], )
    # 12월까지의 계산 결과 or 1년권
    min_cost = min(plans[12], cost[3])
    print(f"#{tc} {min_cost}")