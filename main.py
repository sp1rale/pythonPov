start = int(input('Введіть почаьок діапазону'))
end = int(input('Ведіть кінець діапазону'))

print(f"Всі числа в діапазоні: {list(range(start, end+1))}")

print(f"Всі числа в діапазоні в спадному порядку: {list(range(end, start-1, -1))}")

multiples_of_7 = [num for num in range(start, end+1) if num % 7 == 0]
print(f"Числа, кратні 7: {multiples_of_7}")

multiples_of_5 = len([num for num in range(start, end+1) if num % 5 == 0])
print(f"Кількість чисел, кратних 5: {multiples_of_5}")

