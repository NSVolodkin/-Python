clock = int(input("введите вермя в секундах\n"))
hours = clock//3600
minetes = (clock - hours * 3600) // 60
secunds = clock % 60
print(f"время {hours:>02}:{minetes:>02}:{secunds:>02}")