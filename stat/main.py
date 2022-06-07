from scipy.stats import kstest
import matplotlib.pyplot as pl
import pandas as p


a = p.read_csv('stat.csv')
pl.bar(a['Age'], a['Num'])
a = p.DataFrame(data={'Num': a['Num']})['Num']

s, p = kstest(a, 'norm', (a.mean(), a.std()))
print('Значение p={}'.format(p))
if p > 0.05:
    print('Распределение норм')
else:
    print('эх, не повезло, не повезло')

pl.show()
