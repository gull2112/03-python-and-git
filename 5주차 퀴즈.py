#  1
def add(a, b, c, d):
    return a + b + c + d


def multiply(a, b, c, d):
    return a * b * c * d


print(add(1, 3, 5, 7))  # 출력: 16
print(multiply(1, 3, 5, 7))  # 출력: 105


#  2
def number(a):
    if a % 2 == 0:
        return "짝수"
    else:
        return "홀수"


print(number(7))  # 출력: 홀수
print(number(4))  # 출력: 짝수


#  3
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average([1, 3, 5, 7, 9]))


#  4
class partner:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")


character = partner("wizard", "여성", "마법사")
character.attack()


#  5
class property:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def information(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")


estate = property("인천", 35, "아파트", 350000000, 2009)
estate.information()