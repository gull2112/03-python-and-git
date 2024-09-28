#1
if input("문자를 입력해주세요:") == "안녕하세요" :
    print("반갑습니다")
else :
    print("인사를 먼저하세요")
#2
numbers = int(input("값을 입력하세요"))
a = numbers + 100
if a >= 150 :
    print(a)
elif a <= 150 :
    print("값이 부족합니다")
#3
results = []

numbers = [100,200,300]

for a in numbers:
   b= a * 1.1
   results.append(b)
print(results)

# 4
numbers = [3, 100, 23, 33, 72, 94]
result = []

for a in numbers:
    if a % 3 == 0:
        result.append(a)
print(result)

# 5
a = 1
while a <= 1000:
    print(a)
    a=a+1

# 6
a = 1
sum = 0
while a <= 100:
    if a % 2 != 0:
        sum += a
    a += 1
print(sum)

