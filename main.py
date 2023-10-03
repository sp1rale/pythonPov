start = int(input('Введіть початок діапазону'))
end = int(input('Введіть кінець діапазону'))

for num in range(start, end + 1):
    if num % 7 == 0:
        print(num)