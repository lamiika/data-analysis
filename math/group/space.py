import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats

def pvalue_test(out, sig, task):
    if out.pvalue < sig:
        print(f'{task} eroaa merkitsevästi {out.pvalue} < {sig}')
    else:
        print(f'{task} ei eroa merkitsevästi {out.pvalue} >= {sig}')
        
# kahden otoksen keskiarvon vertailu
sig = 0.05
R1 = [31, 47.5, 36, 54, 57, 48, 40, 54.5, 100]
R2 = [42, 127, 30, 64, 43, 55, 153]
R3 = [32, 35, 48, 70, 32, 23, 74]
R4 = [31, 35, 30, 55.5, 50, 52, 31]

squares = [R1, R2, R3]
for r in squares:
    out = stats.ttest_ind(R4, r, alternative='greater', equal_var=False)
    print(out.statistic)
    pvalue_test(out, sig, 'Pinta-alat')
    
    
    