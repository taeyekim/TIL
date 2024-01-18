
import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data[0])

# dummy_data = []
# for i in range(10) :
#     temp_dict = {'company': parsed_data['company']['name'],
#                  'lat': parsed_data[]
#                  }
#     dummy_data.append(temp_dict)
    
    
# print(dummy_data)
    
print(parsed_data[0]['company'])