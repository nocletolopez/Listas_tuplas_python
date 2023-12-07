"""slicing reasignar valor
numero = ["como te llamas",23,18,"te quiero",9]
numero = numero [0:3] + "23" + numero [2:]
"""
#slicing (desafio)
numero = ["como te llamas",23,18,"te quiero",9]
numero_2 = ["conocer",1,2,3,"donde", "cuando"]

numero.append(456789)
numero.append("Hola mundo")

numero_2.append("Hola y adiós")
numero_2.append(5555)

numero_3 = numero.pop()
numero_4 = numero_2.pop()
numero_4 = numero_2[1::]
numero_4.pop()

lista = [numero_4] + [numero_3]
print(lista)

