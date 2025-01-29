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

print("1a) Alle 169 cm pitkiä miehiä: ", round(percentage_under_169, 1), "%")

# 1 b
print("1b) Yli 169 cm pitkiä miehiä: ", round(100 - percentage_under_169, 1), "%")

# 1 c
x = 187
percentage_over_187 = 100 - stats.norm.cdf(x, loc=mean, scale=std_dev) * 100
print("1c) Yli 187 cm pitkiä miehiä: ", round(percentage_over_187, 1), "%")

# 1 d 
percentage_169to187 = 100 - percentage_under_169 - percentage_over_187
print("1d) Välillä 169 - 187 cm: ", round(percentage_169to187, 1), "%")

# 1 e
lower = 160
upper = 196

percentage_160to196 = (100 * 
(stats.norm.cdf(upper, loc=mean, scale=std_dev) - 
 stats.norm.cdf(lower, loc=mean, scale = std_dev)))
print("1e) Välillä 160 - 196 cm: ", round(percentage_160to196, 1), "%")

# 2 a, b, c, d
values = [169, 187, 160, 196]
for i in values:
    print("2) ", i, "cm normeerattuna: ", (i - mean) / std_dev)

# 4 a
mean = 178
std_dev = 9
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
y = stats.norm.pdf(x, mean, std_dev)

plt.plot(x,y)
plt.title("4a) suomalaisten miesten normaalijakauma")
plt.show()

# 4 b
mean = 0
std_dev = 1
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
y = stats.norm.pdf(x, mean, std_dev)

plt.plot(x,y)
plt.title("4b) standardinormaalijakauma")
plt.show()

# 5
data = [180, 175, 185, 179]
for i in data:
    print("5) ", i, ": ", (i - 178) / 9)

# 6 a
mean = 0
std_dev = 1
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
y = stats.norm.pdf(x, mean, std_dev)

plt.plot(x,y, linestyle="dashed", label="Norm.", zorder=6)

# 6 b
df = 1
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 1000)
plt.plot(x, stats.t.pdf(x, df), label="t1", zorder=5)

# 6 c
df = 3
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
plt.plot(x, stats.t.pdf(x, df), label="t3", zorder=4)

df = 5
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
plt.plot(x, stats.t.pdf(x, df), label="t5", zorder=3)

# 6 d
df = 30
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
plt.plot(x, stats.t.pdf(x, df), label="t30", zorder=2)

df = 1000
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
plt.plot(x, stats.t.pdf(x, df), label="t1000", zorder=1)
plt.xlim(-5, 5)
plt.legend()
plt.title("6) Normaalijakauma vs. t-jakaumia")
plt.show()

# Suuren vapausasteen kuvaajat lähestyvät normaalijakaumaa.
# Muoto ei juuri muuta muotoaan, kun mennään 
# suuresta vapausasteesta vielä suurempaan.

# 7 a
a = [178, 190, 166, 175, 181]
mean = np.mean(a)
print("7a) keskiarvo: ", mean)

# 7 b
merkitsevyystaso = 0.05
out = stats.ttest_1samp(a, 180)

if out.pvalue < merkitsevyystaso:
    print("7b) Hylätään nollahypoteesi")
else:
    print("7b) Hyväksytään nollahypoteesi")
print("7b) ", out.pvalue, " (63.6%) > 0.05 (5%) eli ei eroa tilastollisesti merkitsevästi")

# 8 a
am = [171, 183, 159, 168, 174]
mean = np.mean(am)
print("8a) keskiarvo: ", mean)

# 8 b
merkitsevyystaso = 0.05
out = stats.ttest_1samp(am, 180)

if out.pvalue < merkitsevyystaso:
    print("8b) Hylätään nollahypoteesi")
else:
    print("8b) Hyväksytään nollahypoteesi")
print("8b) ", out.pvalue, " (8.3%) > 0.05 (5%) eli ei eroa tilastollisesti merkitsevästi")

# 9
merkitsevyystaso = 0.05
out = stats.ttest_1samp(a, 189)

if out.pvalue < merkitsevyystaso:
    print("9) Hylätään nollahypoteesi")
else:
    print("9) Hyväksytään nollahypoteesi")
print("9) ", out.pvalue, " (4.8%) < 0.05 (5%) eli kyllä eroaa tilastollisesti merkitsevästi")

# 10
merkitsevyystaso = 0.01
out = stats.ttest_1samp(a, 189)

if out.pvalue < merkitsevyystaso:
    print("10) Hylätään nollahypoteesi")
else:
    print("10) Hyväksytään nollahypoteesi")
print("10) ", out.pvalue, " (4.8%) > 0.01 (1%) eli ei eroa tilastollisesti merkitsevästi")
