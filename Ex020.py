from random import shuffle

n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('ultimo aluno:'))
lista = [n1, n2, n3, n4]
ordem = shuffle(lista)
print('a ordem dos alunos que apresentaram o trabalho será:\n {}'.format(lista))
