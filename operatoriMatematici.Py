import math
import random


num1 = 6
num2=9.3
somma=num1+num2
prodotto=num1*num2
differenza=num1-num2
quoziente=num1/num2

print("=== Stampo i risultati===")
print(f"somma:{somma}")
print(f"Prodotto:{prodotto}")
print(f"Differenza:{differenza}")
print(f"Quoziente:{quoziente}")
print("=========================")

calcolo = 0.1 + 0.2
print(calcolo)
print(round(calcolo,2))

calcolo2 = 0.1 * 0.2
print(calcolo2)
print(round(calcolo2, 2))

#operatore modulo o resto della divisione
mod1 = 4 % 2
print(f"Il resto di questa divisione vale:{mod1}")
mod2 = 4%3
print(mod2)
mod3= 6%8
print(mod3)

miaVar= 1
#voglio incrementare la mia variabile di 5
miaVar += 5 
print(miaVar)

miaVar *= 3
print(miaVar)

miaVar -= 1
print(miaVar)

miaVar /= 6
print(miaVar)

# Elevamento a potenza 
mioNum = 6

pow1= mioNum** 2
print(f"La potenza di {mioNum} elevato a 2 vale {pow1}")

radice1 = 9**0.5
print(f"la radice di 9 vale{radice1}")

potenza2 = pow(5, 2 ) #pow() è una funzione matematica built in 
print(potenza2)

radice2 = math.sqrt(81) #math è una libreria che va obbligatoriamente importata di solito tutti gli import avvengono in alto nella pagina o quantomeno prima di utilizzarli 
print(radice2)


numCas= random.random()
print(numCas)
numCas2 = random.randint(1,10)
print(numCas2)
