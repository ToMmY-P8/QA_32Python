#Завдання №3

m = float(input("Введіть кількість, м: "))
mi=m/1609.34
inch=m*39.37
yd=m*1.094

choise=float(input("Виберіть одиницю виміру:\n1 - Милі\n2 - Дюйми\n3 - Ярди\n"))
if choise == 1:
    print("Милі, mi: ", round(mi,4))
elif choise ==2:
    print ("Дюйми, in: ", round(inch, 2))
elif choise ==3:
    print ("Ярди, yd: ", round(yd, 2))