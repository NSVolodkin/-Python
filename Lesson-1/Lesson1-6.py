a = int(input("Скольтко спортсмен пробегал в первый день\n"))
b = int(input("Сколько спортсмен доожен пробежать всего\n"))

tmp = a
result = 1

while b >= tmp:
    tmp += tmp * 1.1
    result += 1
print("Спортсмен пробежит", b, "километров за", result, "дней")