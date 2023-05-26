



x = int(input("Введите число X: "))
y = int(input("Введите число Y: "))
if x <= 1000 and y <= 1000:
    print ("Принято. Работаем дальше")
    for i in range(x):
        for j in range(y):
            if x == i + j and y == i * j:
                print(i, j)
else:
    print ("Цифра неправильная")
    
