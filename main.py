num = int(input("Введіть число: "))

factorial_sum = 0

if num > 0:
    for i in range(1, num + 1):
        factorial_sum += i
    print(f"Факторіал числа {num} дорівнює {factorial_sum}")
else:
    print("Будь ласка, введіть додатне число.")