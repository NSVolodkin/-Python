profit = int(input("Укажите выручку фирмы\n"))
expenses = int(input("Укажите издержки фирмы\n"))
if profit > expenses:
    print("Вы работаете с прибылью")
    print("Рентабильность бизнеса", profit / expenses)
    people = int(input("Введите численность сотрудников\n"))
    print("Прибыль на каждого сотрудника =", profit / people)
else:
    print("Вы работаете в убыток")
