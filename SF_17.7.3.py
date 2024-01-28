per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты:'))
rate = list(per_cent.values())
#deposit = [rate[0]*money, rate[1]*money, rate[2]*money, rate[3]*money]
deposit = [i * money for i in rate]
deposit = list(map(int,deposit))
print ('deposit =',deposit)
max_income = max(deposit)
print ('Максимальная сумма, которую вы можете заработать —', max_income)