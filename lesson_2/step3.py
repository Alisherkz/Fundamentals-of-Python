num = int(input("Число месяца: "))

month = ["Весна", "Лето", "Осень", "Зима"]

if num == 3 or num == 4 or num == 5:
    print(month[0])
elif num == 6 or num == 7 or num == 8:
    print(month[1])
elif num == 9 or num == 10 or num == 11:
    print(month[2])
else:
    print(month[3])
