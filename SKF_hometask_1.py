per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))

percent = list(map(float,per_cent.values()))
deposit = list([money*0.01*i for i in percent]) #непонятно, как сделать без цикла

print("Максимальная сумма, которую вы можете заработать ", round(max(deposit),2))
