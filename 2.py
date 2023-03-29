#Elabore um programa python que permita calcular a média de um aluno atendendo às notas obtidas em 
#dois testes. O programa deve apresentar se o aluno foi aprovado ou reprovado, tendo em conta que um 
#aluno aprova sempre que a média é superior ou igual a 10 valores.

nota1 = float(input("Insira o valor da primeira nota: "))

nota2 = float(input("Insira o valor da segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 9.5):
    print("O aluno está aprovado com %s valores!" % media)    

elif(media <= 9.5):
    print("O aluno está reprovado :(")