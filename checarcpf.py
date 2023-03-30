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
