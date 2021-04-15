# 함수를 호출할 때 매개변수를 지정할 수 있다.
# 구조
def add(a,b):
    return a + b

number = add(a=3, b=7)  # a에 3, b에 7를 전달
print(number)

# >> 이렇게 매개변수를 지정하면 순서와 상관없이 사용할 수 있다.

number = add(b=5, a=3) # b에 5, a에 3를 전달
print(number)
