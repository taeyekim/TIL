class Person:
    # 속성
    blood_color = 'red'

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다'
    
singer1 = Person('IU')
singer2 = Person('BTS')
# 메서드를 호출
print(singer1.singing())
print(singer2.singing())

print(singer1.blood_color)