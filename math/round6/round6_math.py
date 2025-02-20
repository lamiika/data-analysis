import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats

def pvalue_test(out, sig, task):
    if out.pvalue < sig:
        print(f'{task}) eroaa merkitsevästi {out.pvalue} < {sig}')
    else:
        print(f'{task}) ei eroa merkitsevästi {out.pvalue} >= {sig}')

# 1 a
lsat = [576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594]

lsat_comparison = [663, 614, 649, 643, 676]

sig = 0.05

out = stats.ttest_ind(lsat, lsat_comparison)

pvalue_test(out, sig, '1a')

# 1 b
print('Populaatioilla tulee olla identtiset varianssit.')
print('Populaatiot noudattavat normaalijakaumaa.')
print('Otosten tulisi olla itsenäisiä toisistaan.')

# 2 a
a = [178, 190, 166, 175, 181]
aM = [166, 179, 155, 164, 170]

a_var = np.square(np.std(a))
aM_var = np.square(np.std(aM))
difference = a_var - aM_var

print(f'2a) a_var {a_var} - aM_var {aM_var} = {difference}.')
print('Tulos on lähellä 0 joten varianssit ovat suunnilleen samat.')

# 2 b
sig = 0.05

out = stats.ttest_rel(a, aM)

pvalue_test(out, sig, '2b')

# 2 c
print('2c) a-kohdassa varmistettiin t-testin alkuoletus että varianssi on sama')

# 3
sig = 0.05
def chi_square_variance(sample, exp):
    n = len(sample)
    obs = np.std(sample)
    chi_statistic = (n-1) * np.square(obs / exp)
    df = n - 1
    pvalue = 1 - stats.chi2.cdf(chi_statistic, df)
    if pvalue < sig:
        print(f'3) eroaa merkitsevästi {pvalue} < {sig}')
    else:
        print(f'3) ei eroa merkitsevästi {pvalue} >= {sig}')
    
mileage1 = [7.0642, 7.0431, 7.1501, 7.2159, 7.2381, 7.1285]
mileage2 = [6.8185, 6.7597, 6.9597, 7.0431, 6.9804, 6.9392]
mileage3 = [6.2898, 6.3924, 6.2564, 6.4273, 6.3578, 6.4098]
exp = 0.9

chi_square_variance(mileage1, exp)
chi_square_variance(mileage2, exp)
chi_square_variance(mileage3, exp)


# 4
sig = 0.001
task = '4'
out12 = stats.ttest_ind(mileage1, mileage2)
out13 = stats.ttest_ind(mileage1, mileage3)
out23 = stats.ttest_ind(mileage2, mileage3)

pvalue_test(out12, sig, task)
pvalue_test(out13, sig, task)
pvalue_test(out23, sig, task)

# 5 a
a = [178, 190, 166, 175, 181]
aM = [166, 179, 155, 164, 170]
a_avg = np.average(a)
aM_avg = np.average(aM)
sig = 0.05

out = stats.ttest_ind(a, aM)
pvalue_test(out, sig, '5a')

# 5 b
out = stats.ttest_ind(aM, a, alternative='less')
pvalue_test(out, sig, '5b')

# 5 c
sig = 0.01
out = stats.ttest_ind(a, aM)
pvalue_test(out, sig, '5c')
out = stats.ttest_ind(aM, a, alternative='less')
pvalue_test(out, sig, '5c')

# 6 a
sig = 0.05
data = [51, 59, 40, 47, 53]
n = len(data)
customers = 200
even_customers = customers / n

out = stats.chisquare(data)
pvalue_test(out, sig, '6a')
print('6a) Ei eroa merkitsevästi eli dataa voidaan pitää tasajakautuneena')

# 6 b
out = stats.shapiro(data)
pvalue_test(out, sig, '6b')
print('6b) Shapiro nollahypoteesi hyväksytty eli data on peräisin normaalijakaumasta')

# 7
def ethnicity_test(out, sig, index):
    if out.pvalue[index] < sig:
        print(f'7) etnisyys {index + 1} eroaa merkitsevästi {out.pvalue[index]} < {sig}')
    else:
        print(f'7) etnisyys {index + 1} ei eroa merkitsevästi {out.pvalue[index]} >= {sig}')

data = np.array([[936, 240, 195, 101], [909, 297, 150, 115]])
sig = 0.05

out = stats.chisquare(data)
for i in range(4):
    ethnicity_test(out, sig, i)
