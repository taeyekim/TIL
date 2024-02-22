import math

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

import math

def calculate_distance(point1, point2):
    """두 점 사이의 거리를 계산합니다."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_shot_angle(white_ball, target_ball, hole):
    # 각 변의 길이 계산
    a = calculate_distance(target_ball, hole)  # 목적구에서 홀까지
    b = calculate_distance(white_ball, target_ball)  # 흰 공에서 목적구까지
    c = calculate_distance(white_ball, hole)  # 흰 공에서 홀까지

    # 제2코사인 법칙을 사용하여 각도 계산
    angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
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

# 가장 쉬운 홀 찾기
easiest_hole, min_angle = find_easiest_hole(white_ball_position, target_ball_position, holes)
print(f"Easiest Hole: {easiest_hole}, Shot Angle: {min_angle:.2f} degrees")

