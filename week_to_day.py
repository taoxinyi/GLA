import os

f1 = 'files_detail_'
f2 = 'methods_detail_'

week = 'ww50'
days = ['2018-12-9', '2018-12-10', '2018-12-11', '2018-12-12', '2018-12-13', '2018-12-14', '2018-12-15', '2018-12-16', '2018-12-17']

for i in days:
    os.system('cp ' + f1 + week + '.csv ' + f1 + i + '.csv')
    os.system('cp ' + f2 + week + '.csv ' + f2 + i + '.csv')
