import random

print("Tehtävä 1")
print("Hello world")

print("\nTehtävä 2")
a = input("Anna luku a:")
b = input("Anna luku b:")

if a > b:
    print("a suurempi")
elif a < b:
    print("b suurempi")
else:
    print("yhtäsuuret")
    
print("\nTehtävä 3")
import random 
    
a = random.randint(0, 100)
b = random.randint(0, 100)

print(f"a = {a} b = {b}")

if a > b:
    print("a suurempi")
elif a < b:
    print("b suurempi")
else:
    print("yhtäsuuret")
    
print("\nTehtävä 4")
import random 
    
a = random.randint(0, 10)
b = random.randint(0, 10)
print(f"Lukujen {a} ja {b} summa on: {a+b}")

print("\nTehtävä 5")
import random 
l1 = []
l2 = []
user_input = []
answers = []
correct_amount = 0
for i in range(5):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    l1.append(a)
    l2.append(b)
    answers.append(a*b)
    ans = int(input(f"{a} * {b} = "))
    user_input.append(ans)
    
for i in range(5):
    if user_input[i] == answers[i]:
        print(f"Oikein :-) {l1[i]} * {l2[i]} = {answers[i]}")
        correct_amount += 1
    else:
        print(f"Väärin :-( Oikea vastaus on: {l1[i]} * {l2[i]} = {answers[i]}")
        
print(f"Sait {correct_amount} oikein!")
      
print("\nTehtävä 6")  
import random 
class Murtoluku:
    def __init__(self, osoittaja, nimittaja):
        self.osoittaja = osoittaja
        self.nimittaja = nimittaja
        
    def tulosta(self):
        print(f"{self.osoittaja} / {self.nimittaja}")
        
    def sievenna(self):
        a = self.osoittaja
        b = self.nimittaja
        
        while b != 0:
            t = b
            b = a % b
            a = t
            
        self.osoittaja = self.osoittaja // a
        self.nimittaja = self.nimittaja // a
        
luku = Murtoluku(34562, 311058)
luku.tulosta()
luku.sievenna()
luku.tulosta()

print("\nrandom next\n")

osoittaja = random.randint(0, 1000000)
nimittaja = random.randint(0, 1000000)

luku2 = Murtoluku(osoittaja, nimittaja)
luku2.tulosta()
luku2.sievenna()
luku2.tulosta()
