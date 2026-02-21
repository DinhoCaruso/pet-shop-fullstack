# Crie um programa que tenha uma TUPLA com várias palavras (Não usar ACENTOS).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ("nomade", "bule", "professor", "amigo", "amor", "clara")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')











