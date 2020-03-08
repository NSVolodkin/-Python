user_input = input("введите целое положительное число")

num = int(user_input)
result = 0

while num:
    tmp = num % 10
    if tmp > result:
        result = tmp
    num //= 10
    break
print(result)



