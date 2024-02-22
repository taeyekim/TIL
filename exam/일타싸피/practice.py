import math

def calculate_shot_angle(white_ball, target_ball, hole):
    # 흰 공에서 목적구까지의 벡터를 계산합니다.
    target_vector = (target_ball[0] - white_ball[0], target_ball[1] - white_ball[1])
    # 목적구에서 홀까지의 벡터를 계산합니다.
    hole_vector = (hole[0] - target_ball[0], hole[1] - target_ball[1])

    # 두 벡터의 내적을 계산합니다. 내적은 두 벡터 사이의 각도 정보를 포함합니다.
    dot_product = target_vector[0] * hole_vector[0] + target_vector[1] * hole_vector[1]
    # 두 벡터의 크기(마그니튜드)를 계산합니다.
    magnitude_target = math.sqrt(target_vector[0]**2 + target_vector[1]**2)
    magnitude_hole = math.sqrt(hole_vector[0]**2 + hole_vector[1]**2)
    # 코사인 각도를 계산합니다. 이 값은 두 벡터 사이의 각도의 코사인 값입니다.
    cos_angle = dot_product / (magnitude_target * magnitude_hole)
    
    # 수치 오류로 인해 코사인 값이 -1보다 작거나 1보다 클 수 있으므로, 이를 제한합니다.
    cos_angle = max(min(cos_angle, 1), -1)
    
    # 코사인의 역함수(아크코사인)을 사용하여 각도를 구합니다. 결과는 라디안입니다.
    angle = math.acos(cos_angle)
    # 라디안 값을 도로 변환합니다.
    angle_in_degrees = math.degrees(angle)

    return angle_in_degrees

def find_easiest_hole(white_ball, target_ball, holes):
    easiest_hole = None
    min_angle = 360  # 가능한 최대 각도로 시작합니다.

    # 모든 홀에 대해 반복하며 각 홀까지의 각도를 계산합니다.
    for hole in holes:
        shot_angle = calculate_shot_angle(white_ball, target_ball, hole)
        # 더 작은 각도를 찾으면, 그 홀을 '가장 쉬운 홀'로 간주합니다.
        if shot_angle < min_angle:
            min_angle = shot_angle
            easiest_hole = hole

    # 가장 쉬운 홀과 그때의 각도를 반환합니다.
    return easiest_hole, min_angle

# 내 공(흰 공)과 목적구(빨간 공)의 위치를 설정합니다.
white_ball_position = (20, 30)
target_ball_position = (190, 120)
# 6개의 홀 위치를 설정합니다.
holes = [
    (0, 0),
    (127, 0),
    (254, 0),
    (0, 127),
    (127, 127),
    (254, 127)
]

# 가장 쉬운 홀을 찾기 위해 함수를 호출합니다.
easiest_hole, shot_angle = find_easiest_hole(white_ball_position, target_ball_position, holes)
print(f"Easiest Hole: {easiest_hole}, Shot Angle: {shot_angle} degrees")

import turtle

pool_table_length = 254
pool_table_width = 127
# 당구대를 그리는 함수
def draw_pool_table():
    turtle.penup()
    turtle.goto(-pool_table_length / 2, -pool_table_width / 2)
    turtle.pendown()
    turtle.setheading(90)  # 위로 향하게 초기 방향 설정
    for _ in range(2):
        turtle.forward(pool_table_width)
        turtle.right(90)
        turtle.forward(pool_table_length)
        turtle.right(90)

# 홀을 그리는 함수
def draw_holes():
    for hole in holes:
        turtle.penup()
        turtle.goto(hole[0] - pool_table_length / 2, hole[1] - pool_table_width / 2)
        turtle.dot(12, "black")  # 홀은 검은색 점으로 표시

# 공을 그리는 함수
def draw_ball(position, color):
    turtle.penup()
    turtle.goto(position[0] - pool_table_length / 2, position[1] - pool_table_width / 2)
    turtle.dot(20, color)  # 공의 크기를 도트로 표시

# 경로를 그리는 함수
def draw_shot_path(white_ball, target_ball, hole):
    # 흰 공에서 목적구까지
    turtle.penup()
    turtle.goto(white_ball[0] - pool_table_length / 2, white_ball[1] - pool_table_width / 2)
    turtle.pendown()
    turtle.goto(target_ball[0] - pool_table_length / 2, target_ball[1] - pool_table_width / 2)
    
    # 목적구에서 홀까지
    turtle.goto(hole[0] - pool_table_length / 2, hole[1] - pool_table_width / 2)

# 화면 설정
turtle.Screen().setup(width=800, height=400)  # 화면 크기 설정
turtle.Screen().bgcolor("green")  # 당구대 색상
turtle.speed(0)  # 그리는 속도 설정
turtle.hideturtle()  # 거북이 커서 숨기기

# 당구대, 홀, 공 그리기
draw_pool_table()
draw_holes()
draw_ball(white_ball_position, "white")
draw_ball(target_ball_position, "red")

# 가장 쉬운 홀로의 경로 그리기
draw_shot_path(white_ball_position, target_ball_position, easiest_hole)

# 화면을 닫을 때까지 유지
turtle.done()
