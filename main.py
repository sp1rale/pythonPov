start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

total = 0
count = 0

for num in range(start, end + 1):
    total += num
    count += 1

average = total / count

print(f"Сума чисел у діапазоні: {total}")
print(f"Середньоарифметичне: {average}")