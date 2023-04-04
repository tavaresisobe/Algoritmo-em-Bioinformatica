# 52998224725
# https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/

cpf = (input("Digite seu CPF (apenas números): "))
aux = []
aux_2 = []
for i in range(9):
    n = int(cpf[i]) * (10 - i)
    aux.append(n)
s = sum(aux)
check_1 = s * 10 / 11
print (check_1)

for i in range(10):
    m = int(cpf[i]) * (11 - i)
    aux_2.append(m)
s_2 = sum(aux_2)
print(s_2)
check_2 = s * 10 / 11
print(check_2)


################################################
import random
cpf = [random.randint(0,10) for i in range (9)]
p1 = list(range(11:1:-1))

d1 = [i * j for i, j in zip(l,p1)]
d1 = sum(d1)%11

if d1 < 2:
    d1 = 0
else
    d1 = 11 - d1
cpf.append(d1)

p2 = list(range(11:1:-1))

d2 = [i * j for i, j in zip(l,p2)]
d2 = sum(d2)%11

if d2 < 2:
    d2 = 0
else
    d2 = 11 - d2
cpf.append(d2)

for i in cpf:
    imprime += str(i)


