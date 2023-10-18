#Завдання №2

num1 = float(input("Введіть число №1: "))
num2 = float(input("Введіть число №2: "))
num3 = float(input("Введіть число №3: "))

max = max(num1, num2, num3)
min = min(num1 , num2, num3)
avg = sum((num1, num2, num3))/3

choise=float(input("Виберіть значення чисел:\n1 - Максимум\n2 - Мінімум\n3 - Середнє арифметичне\n"))
if choise == 1:
    print("Максимум: ", max)
elif choise ==2:
    print ("Мінімум: ", min)
elif choise ==3:
    print ("Середнє арифметичне: ", round(avg, 2))