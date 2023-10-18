#Завдання №1

num1 = int(input("Введіть число №1: "))
num2 = int(input("Введіть число №2: "))
num3 = int(input("Введіть число №3: "))

sum = sum((num1, num2, num3))
dob = num1 * num2 * num3

choise=int(input("Виберіть спосіб обчислення:\n1 - Сума\n2 - Добуток\n"))
if choise == 1:
    print("Сума чисел: ", sum)
elif choise ==2:
    print ("Добуток чисел: ", dob)
    