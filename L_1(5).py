revenue = int(input("Введите значения выручки фирмы: "))
cost = int(input("Введите значения издержек фирмы: "))
fin_resul = revenue - cost
if fin_resul <= 0:
    print("Фирма претепевает убыток")
else:
        print("Фирма в прибыли")
        profit = fin_resul/revenue
        print("Рентабельность фирмы", profit)
        quanti = int(input("Введите количество сотрудников: "))
        profit_empl =profit/quanti
        print("Прибыль фирмы в рассчете на одного сотрудника: ", profit_empl)
