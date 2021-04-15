# 입력값과 결괏값에 따른 함수의 형태

# 1. 일반적인 함수
def add(a, b): 
    result = a + b 
    return result
a = add(3, 4)
print (a)


# 2. 입력값이 없는 함수
def say():
    return 'hi'

a = say()
print(a)


# 3. 결과값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % ( a, b, a+b) ) 

a = add(3, 4) 
print(a)


# 4. 입력값도 결과값도 없는 함수
def say():
    print('hi')

say()
