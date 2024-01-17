number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    user_info = dict(name=name, age=age, address=address)
    increase_user()
    print(f"{name}님 환영합니다!")
    return user_info

print("현재 가입 된 유저 수 : " + str(number_of_people))
print(create_user('홍길동', 30, '서울'))
print("현재 가입 된 유저 수 : " + str(number_of_people))
