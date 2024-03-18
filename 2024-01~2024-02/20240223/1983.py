# 1983. 조교의 성적 매기기

T = int(input())
grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for tc in range(1, T+1):
    N, K = map(int, input().split())
    grade = [list(map(int, input().split()) for _ in range(N))]
    student = []
    for i in range(N):
        total = grade[i][0] * 0.35 + grade[i][1] * 0.45 + grade[i][2] * 0.2
        student.append(total)

    print(grade)
