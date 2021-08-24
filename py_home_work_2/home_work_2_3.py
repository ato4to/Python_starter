print('Enter a (only one)')
value_a: int = input()  # ввод первого числа

print('Enter b (only one)')
value_b: int = input()  # ввод второго числа

print('Enter c (only one)')
value_c: int = input()  # ввод третьего числа

if value_a <= value_b and value_b <= value_c:  # сравнение чисел и вывод резутата
    print("True")
else:
    print("False")