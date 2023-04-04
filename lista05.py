# 1) Faça um programa que leia o nome RA e média final de uma aluno. Armazene todas
# as informações num dicionário. No final programa deve imprimir as informações do
# dicionário e situação do aluno (reprovado, exame ou aprovado). Utilize as regras da UNIFESP para
# definir a situação do aluno.

dic = {}
nome = input("Digite o nome completo do aluno: ")
ra = input("Digite o RA: ")
media_f = float(input("digite a média final do aluno: "))

dic ['Nome'] = nome
dic ['RA'] = ra
dic['Média final'] = media_f

for i,j in dic.items():
     print(f"{i}: {j}")

if media_f >= 6.0:
    print ("Aluno aprovado")
elif media_f >= 3.0:
    print ("Exame")
else:
    print ("Aluno reprovado")
