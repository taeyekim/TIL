# 1. 재귀 - 숫자 이어붙이기
# 2. 7자리까지 반복
# 3. 중복 제거 - set, dictionary

# import sys
# sys.stdin = open("input.txt", "r")
#
# def dfs(y, x, path):
#     # 기저조건: 7자리면 끝
#     if len(path) == 7:
#         # 현재까지의 경로를 저장
#         result.add(path)
#         return
#
#     for i in range(4):
#         new_y = y + dy[i]
#         new_x = x + dx[i]
#
#         # 범위 밖으로 넘어가면 pass
#         if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
#             continue
#
#         dfs(new_y, new_x, path + maps[new_y][new_x])
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     # 격자판 저장
#     # 갈 때마다 경로를 더하기 위해서 문자열로 저장
#     maps = [input().split() for _ in range(4)]
#     # 중복을 제거하기 위해 set 사용
#     result = set()
#
#     # 시작 지점
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, maps[i][j])
#     print(f'#{tc} {len(result)}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x, path):
    if len(path) == 7:
        result.append(path)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx <= 3 and 0 <= ny <= 3:
            dfs(ny, nx, path + arr[ny][nx])

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = []
    for y in range(4):
        for x in range(4):
            dfs(y, x, arr[y][x])
    result = set(result)
    print(f"#{tc} {len(result)}")