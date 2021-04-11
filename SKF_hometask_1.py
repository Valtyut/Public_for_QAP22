per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
percent = list(map(float,per_cent.values()))
#print(percent) для проверки
deposit = [money*0.01*i for i in percent]
deposit = list(map(int,deposit))

print("Максимальная сумма, которую вы можете заработать ", max(deposit))
