############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calc_total(cart_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    total = 0 # 합계 total = 0 초기화
    for item in cart_list: # cart_list 요소 순회
        total += item_dict[f'{item}'] # item_dict의 key 'item'에 해당하는 value를 total에 합산
    return total # 총합 total 반환


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
item_dict= {
    'apple_pie': 2500,    'banana_milk': 1800,     'coconut_milk': 2000,
    'egg_tart': 2300,    'fruits_cocktail': 3000,    'gum': 1200,
    'hotdog': 2500,    'ice_cream': 3200,    'juice': 2800,
    'keyboard': 35000,  'lotion': 8700
}

cart1 = ['apple_pie', 'ice_cream', 'juice', 'gum', 'banana_milk']
print(calc_total(cart1))    # 11500
cart2 = ['coconut_milk', 'egg_tart', 'fruits_cocktail', 'lotion', 'keyboard']
print(calc_total(cart2))    # 51000
#####################################################
