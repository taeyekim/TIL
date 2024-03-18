import requests
from pprint import pprint as print

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

print(dummy_data)
