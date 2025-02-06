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
<<<<<<< HEAD
s = np.sqrt(s2)
=======
s = np.sqrt(sum)
>>>>>>> 4582cc8bf4c009aa2185ebec34904f81d9962761

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
n = len(lsat)
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
#pvalue = significance_level
#s = np.std(lsat, ddof=1)
#c = (-pvalue) * s / np.sqrt(n) + mean
#print("4d) raja-arvo: ", c)
c = 581
significance_level = 0.05
out = stats.ttest_1samp(lsat, c, alternative="greater")
print("4d) suurin luku on: ", c, " pvalue: ", out.pvalue)

# 5
mean = 61
n = 30
s = 2
expected_value = 60
significance_level = 0.03

pvalue = (mean - expected_value) / (s / np.sqrt(n))

if pvalue < significance_level:
    print("5) asiakaslupaus ei toteudu", out.pvalue)
else:
    print("5) asiakaslupaus toteutuu", out.pvalue)

# 6 a
a = [178, 190, 166, 175, 181]
mean_a = np.mean(a)
aM = [166, 179, 155, 164, 170]
mean_aM = np.mean(aM)

significance_level = 0.05

out = stats.ttest_1samp(a, mean_aM, alternative="greater")

if out.pvalue < significance_level:
    print("6a) ovat tilastollisesti merkitsevästi erisuuret", out.pvalue)
else:
    print("6a) eivät ole tilastollisesti merkitsevästi erisuuret", out.pvalue)
   
# 6 b
out = stats.ttest_1samp(aM, mean_a, alternative="less")

if out.pvalue < significance_level:
    print("6b) on tilastollisesti merkitsevästi pienempi", out.pvalue)
else:
    print("6b) ei ole tilastollisesti merkitsevästi pienempi", out.pvalue)
    
# 6 c
significance_level = 0.01

if out.pvalue < significance_level:
    print("6c) on tilastollisesti merkitsevästi pienempi", out.pvalue)
else:
    print("6c) ei ole tilastollisesti merkitsevästi pienempi", out.pvalue)
   
# 7
accuracy = 0.05
accuracy_target = 0.01

work = accuracy / accuracy_target
print("7) Lisätyön määrä:", work, "kertaa enemmän")
