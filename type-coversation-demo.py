'''
       Daire Alan     : πr2
       Daire çevresi  : 2πr

       * Yarı çapı verilen bir dairenin alan ve çevresini 
       hesaplanıyınız. (r: 3.14)

'''

pi = 3.14

r = float(input("yarı çap: "))


alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan: "+ alan + " çevre:")
