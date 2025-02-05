import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats

# 1 a
a = [178,190,166,175,181]
mean = 178
n = 5
s2 = 0
for i in a:
    s2 = s2 + (i-178)**2/(5 - 1)
s = np.sqrt(sum)

# 1 b
t = (178 - 180) / (s * np.sqrt(5))

# 2 a
am = [171,183,159,168,174]

mean = np.mean(am)
print("2a) Keskiarvo: ", mean)

# 2 b
significance_level = 0.05
c = 180
out = stats.ttest_1samp(am, c, alternative="less")
if out.pvalue < significance_level:
    print("2b) on tilastollisesti merkitsevästi pienempi", out.pvalue)
else:
    print("2b) ei ole tilastollisesti merkitsevästi pienempi", out.pvalue)

# 2 c
print("2c) ", out.pvalue)

# 3 a
a = [7.0642, 7.0431, 7.1501, 7.2159, 7.2381, 7.1285,
     6.8185, 6.7597, 6.9597, 7.0431, 6.9804, 6.9392,
     6.2898, 6.3924, 6.2564, 6.4273, 6.3578, 6.4098]

n = len(a)
mean = np.mean(a)
s = scipy.special.stdtrit(n - 1, 0.03)
print("3a) otoskeskiarvo: ", mean, " otoskeskihajonta: ", s)

# 3 b
c = 6.72
significance_level = 0.005
out = stats.ttest_1samp(a, c)

if out.pvalue < significance_level:
    print("3b) on tilastollisesti merkitsevästi pienempi", out.pvalue)
else:
    print("3b) ei ole tilastollisesti merkitsevästi pienempi", out.pvalue)
    
# 4 a
lsat = [576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594]
mean = np.mean(lsat)
print("4a) keskimääräinen pistemäärä: ", mean)

# 4 b
c = 600
significance_level = 0.05
out = stats.ttest_1samp(lsat, c, alternative="greater")

if out.pvalue < significance_level:
    print("4b) on tilastollisesti merkitsevästi suurempi", out.pvalue)
else:
    print("4b) ei ole tilastollisesti merkitsevästi suurempi", out.pvalue)
    
# 4 c
c = 570
significance_level = 0.05
out = stats.ttest_1samp(lsat, c, alternative="greater")

if out.pvalue < significance_level:
    print("4c) on tilastollisesti merkitsevästi suurempi", out.pvalue)
else:
    print("4c) ei ole tilastollisesti merkitsevästi suurempi", out.pvalue)
   
# 4 d
pvalue = significance_level
s = np.std(lsat, ddof=1)
c = (-pvalue) * s / np.sqrt(n) + mean
print("4d) raja-arvo: ", c)

