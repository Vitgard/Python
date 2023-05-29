# a = int(input('Количество учащихся в 1 классе: '))
# b = int(input('Количество учащихся в 2 классе: '))
# c = int(input('Количество учащихся в 3 классе: '))

# part1 = (a + 1) // 2
# part2 = (b + 1) // 2
# part3 = (c + 1) // 2

# print(part1 + part2 + part3) 


#print(((a + 1) // 2) + ((b + 1) // 2) + ((c + 1) // 2))

# i = int(input('В какой вагон вы сели: '))
# j = int(input('Какой вагон указан: '))

# if i == j:
#     print("Невозможно узнать количество вагонов")
# else:
#     print(f"Общее количество вагонов: {i + j - 1}")



# n = int(input('Введите год '))
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# list_1 = [(i, i * i) for i in range(1, 11) if i % 2 == 0]
# print(list_1)

# n = int(input())
# result = 1
# while n != 1:
#     result *= n
#     n -= 1
# print(result)

# n = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"}]
# values = set()
# for i in n:
#     values.add(list(i.values())[0])
#     for key in i:
#         values.add(i[key])
# print(values)
data = [int(i) for i in input("Введите числа: ").split()]
count = 0
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        count += 1
print(count)






















