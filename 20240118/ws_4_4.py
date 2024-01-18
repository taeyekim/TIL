import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(user_list):
    censored_user_list = []
    for user in user_list:
        temp_data = censorship({f"{user['company']}": f"{user['name']}"})
        if temp_data == True:
            censored_user_list.append({f"{user['company']}": f"{user['name']}"})
    return censored_user_list

def censorship(black_list_check):
    global black_list
    company = list(black_list_check.keys())[0]
    name = list(black_list_check.values())[0]
    if company in black_list:
        print(f"{company} 소속의 {name} 은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
    return True

# python.exe -m pip install --upgrade pip

dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    # dummy_data 리스트에 사용자의 name 추가
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    if (lat < 80 and lat > -80) and (lng < 80 and lng > -80):
        temp_dict = {}
        temp_dict['company'] = parsed_data['company']['name']
        temp_dict['lat']= parsed_data['address']['geo']['lat']
        temp_dict['lng']= parsed_data['address']['geo']['lng']
        temp_dict['name'] = parsed_data['name']
        dummy_data.append(temp_dict)

print(create_user(dummy_data))