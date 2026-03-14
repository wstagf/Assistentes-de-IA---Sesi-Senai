# um professor precisa calcular 
# a media dos alunos
#notas de 0.00 a 10.00... Ex. 7.50, , 
# prova 1 
# prova 2 
# media (prova 1 + prova 2 ) / 2

# escreva = print
# leia = float(input())


n1 = float(input("Digite a primeira nota:"))

if(n1 < 0) or (n1 > 10):
    print("nota invalida")
else:
    n2 = float(input("Digite a segunda nota:"))
    if(n2 < 0) or (n2 > 10):
        print("nota invalida")
    else: 
        media = (n1 + n2) / 2

        print("a media final e")
        print(media)