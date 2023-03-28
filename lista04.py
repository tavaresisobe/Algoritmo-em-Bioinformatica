#1 Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

#list = []
#for i in range(10):
#    x = input(f"Digite o {i+1} número(s): ")
#    list.append(x)
#print (list[::-1])

#2 Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

#lista_1 = []
#lista_2 = []
#lista_aux = []
#while True:
#    aux = input("Digite o(s) elemento(s) da primeira lista:\n(press enter para continuar/digite stop para parar)\n")
#    if aux.upper() == 'STOP':
#        break
#    else:
#        lista_1.append(aux)
#print ("\n\n")
#while True:
#    aux = input("Digite o(s) elemento(s) da segunda lista:\n(press enter para continuar/digite stop para parar)\n")
#    if aux.upper() == "STOP":
#        break
#    else:
#        lista_1.append(aux)

#lista_aux = lista_1 + lista_2
#print (f"A lista gerada foi {lista_aux}")



#3 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4].
#Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

temp = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = temp[0]
menor = temp[0]
for i in len(temp):
    if (temp[i] < menor):
        menor = temp[i]
for i in len(temp):
    if (temp[i] > maior):
        maior = temp[i]
print (f"A Menor temperatura registrada foi {menor}ºC)")
print (f"A Maior temperatura registrada foi {maior}ºC)")
print(f"A Média de Temperatura ficou entre {sum(temp)/2}ºC)")


#4 Faça um Programa que leia 20 números inteiros e armazene-os num lista. Armazene os números pares na lista
#PAR e os números IMPARES na lista impar. Imprima os três vetores.

#lista = []
#par = []
#impar = []

#while True:
#  n = int(input("Informe um número (zero para sair): "))
#  if n == 0:
#    break
#  else:
#    lista.append(n)

#for i in lista:
#  if i % 2 == 0:
#    par.append(i)
#  else:
#    impar.append(i)

#print ("Números pares informados: ", par)
#print("Números ímpares informados: ", impar)

#5 Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada
# aluno, imprima o número de alunos com média maior ou igual a 7.0

