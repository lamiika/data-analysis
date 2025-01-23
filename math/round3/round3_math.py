import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Tuntiesimerkki

x = [180, 175, 185, 179]

merkitsevyystaso = 0.05
out = stats.ttest_1samp(x, 190)

if out.pvalue < merkitsevyystaso:
    print("Hylätään nollahypoteesi")
else:
    print("Hyväksytään nollahypoteesi")

print(out)

# 1 a
mean = 178
std_dev = 9
x = 169

percentage_under_169 = stats.norm.cdf(x, loc=mean, scale=std_dev) * 100

print("Alle 169 cm pitkiä miehiä: ", round(percentage_under_169, 1), "%")

# 1 b
print("Yli 169 cm pitkiä miehiä: ", round(100 - percentage_under_169, 1), "%")

# 1 c
x = 187
percentage_over_187 = 100 - stats.norm.cdf(x, loc=mean, scale=std_dev) * 100
print("Yli 187 cm pitkiä miehiä: ", round(percentage_over_187, 1), "%")

# 1 d 
percentage_169to187 = 100 - percentage_under_169 - percentage_over_187
print("Välillä 169 - 187 cm: ", round(percentage_169to187, 1), "%")

# 1 e
lower = 160
upper = 196

percentage_160to196 = (100 * 
(stats.norm.cdf(upper, loc=mean, scale=std_dev) - 
 stats.norm.cdf(lower, loc=mean, scale = std_dev)))
print("Välillä 160 - 196 cm: ", round(percentage_160to196, 1), "%")

# 2 a - d
values = [169, 187, 160, 196]
for i in values:
    print(i, "cm normeerattuna: ", (i - mean) / std_dev)

# 
