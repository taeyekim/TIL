class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild:
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        "첫째가 응애"

baby1 = FirstChild("김태연")
print(baby1.swim())
print(baby1.cry())
print(baby1.cry)
print(baby1.gene)