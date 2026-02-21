#                                  CONDIÇÕES ANINHADAS
#
#        EXEMPLO DA AULA 10
#
#                                             SE = if, senão = else, senão se = elif
#        carro.siga()                         if, elif e else (dentro de if, pode-se
#        SE CARRO.ESQUERDA()                  utilizar quantos elifs quiser, já os else,
#           carro.siga()                      só podem ser utilizados uma vez ou nenhuma).
#           carro.direita()                   OBS: NUNCA PODE USAR elif SEM O if.
#           carro.siga()
#           carro.direita()
#           carro.esquerda()
#           carro.siga()
#           carro.direita()
#           carro.siga()

#        SENÃO SE CARRO.DIREITA()
#           carro.siga()
#           carro.esquerda()
#           carro.siga()
#           carro.esquerda()
#           carro.siga()
#
#        SENÃO
#           carro.siga()
#        carro.pare()

# EXEMPLO PRATICO

nome = str(input('Qual é o seu nome? '))
if nome == 'Osvaldo':                       #Condição Simples
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #Estrutura Condicional Aninhada
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:                                       #Condição Composta
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')



















