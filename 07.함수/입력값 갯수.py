# [ 여러 개의 입력값을 받는 함수 만들기 ]
def add_many(*args):
    age = 0
    for i in args:
        age = age + i
    return age

age = add_many(16,24,43,47)
print(age)


def add_mul(choice, *args):
    if choice =="add":
        age = 0
        for i in args:
            age = age + i
    elif choice == "mul":
        age = 1
        for i in args:
            age = age * i
    return age

age = add_mul('add', 16,18,42,45)
print(age)

age = add_mul('mul', 16,18,42,45)
print(age)
            

