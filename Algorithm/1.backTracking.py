# 백트래킹
# 완전탐색 + 가지치기
# 가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 기법

# 중복된 순열
# 1~3 까지 숫자 배열이 있을 때
# 111, 112, 113, 121, 122, 123 ... 332, 333

# 재귀 함수 => 특정 시점으로 돌아오는 게 핵심!
# 재귀 함수 팁
# 파라미터: 바로 작성 X
#   구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다!

arr = [i for i in range(1, 4)]
path = [0] * 3

# 순열
# 123, 132, 213, 231, 312, 321
# 조건 : 숫자는 한 번만 사용해라!

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가 ?
    #   - 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재
    # 기본 코드
    # path[level] = arr[0]
    # dfs(level + 1)
    #
    # path[level] = arr[1]
    # dfs(level + 1)
    #
    # path[level] = arr[2]
    # dfs(level + 1)

    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못가! (가지치기)
        # 백트래킹 코드 팁
        # 갈 수 없는 경우를 활용
        # 아래 코드처럼 갈 수 없을 때 continue
        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs(level + 1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0


dfs(0)




