start = int(input('Введіть почаьок діапазону'))
end = int(input('Ведіть кінець діапазону'))

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)