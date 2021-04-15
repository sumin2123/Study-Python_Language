# 리스트 기본 구조
my_list = []
print(my_list)

my_list2 = [1,-2,3.14]
print(my_list2)

my_list3 = ['엘리스', 10,[1.0, 1.2]]
print(my_list3)

# 값 추가하기
clovers = []
clovers.append('클로버1')
print(clovers)

clovers.append('하트2')
print(clovers)

clovers.append('클로버3')
print(clovers)

#값에 접근하기
print(clovers[1])

clovers[1] = '클로버2'
print(clovers)

#값을 제거하기
print(clovers[1])

del clovers[1]
print(clovers)

print(clovers)