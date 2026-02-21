import time

def exibir_ascii_pokebola():
    """Exibe uma arte ASCII de uma Pokébola para a introdução."""
    print("""
          @@@@@@@@@@
       @@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@
    @@@@@@@    @@@    @@@@
   @@@@@@      @@@      @@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@   @@@@@@@@@@@   @@@@
   @@@@     @@@@@     @@@@
    @@@@@           @@@@@
     @@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@
    """)

def soma(x, y):
    """Executa o 'golpe' Growth (Soma)."""
    print("\nUsando o golpe Growth!")
    time.sleep(1) # Pequena pausa para efeito dramático
    return x + y

def subtracao(x, y):
    """Executa o 'golpe' Leer (Subtração)."""
    print("\nUsando o golpe Leer!")
    time.sleep(1)
    return x - y

def multiplicacao(x, y):
    """Executa o 'golpe' Hyper Beam (Multiplicação)."""
    print("\nDisparando um poderoso Hyper Beam!")
    time.sleep(1)
    return x * y

def divisao(x, y):
    """Executa o 'golpe' Cut (Divisão)."""
    if y == 0:
        # Erro temático para divisão por zero
        return "Um Snorlax selvagem apareceu e está bloqueando a divisão por zero! Não é possível continuar."
    print("\nUsando o golpe Cut para dividir!")
    time.sleep(1)
    return x / y

def calculadora_pokemon():
    """Função principal que roda a calculadora."""
    exibir_ascii_pokebola()
    print("==========================================")
    print("    BEM-VINDO À CALCULADORA POKÉMON!    ")
    print("==========================================")
    print("Prepare seus Pokémon (números) para a batalha de cálculos!\n")

    while True:
        print("\nEscolha o seu movimento (operação):")
        print("1. Growth (Soma +)")
        print("2. Leer (Subtração -)")
        print("3. Hyper Beam (Multiplicação *)")
        print("4. Cut (Divisão /)")
        print("5. Flee (Fugir da Batalha)")

        escolha = input("Digite o número do movimento que deseja usar: ")

        if escolha == '5':
            print("\nVocê fugiu da batalha. Até a próxima, Treinador!")
            break

        if escolha in ('1', '2', '3', '4'):
            try:
                # Usando "Level" como tema para os números
                num1 = float(input("\nDigite o Level do primeiro Pokémon (número): "))
                num2 = float(input("Digite o Level do segundo Pokémon (número): "))
            except ValueError:
                print("\nErro! Isso não parece um Level válido. O Professor Carvalho está confuso. Tente novamente.")
                continue

            if escolha == '1':
                resultado = soma(num1, num2)
                print(f"--> O poder combinado dos Pokémon agora é: {resultado}")

            elif escolha == '2':
                resultado = subtracao(num1, num2)
                print(f"--> A diferença de poder entre os Pokémon é: {resultado}")

            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
                print(f"--> O poder foi amplificado! O resultado é: {resultado}")

            elif escolha == '4':
                resultado = divisao(num1, num2)
                if isinstance(resultado, str): # Verifica se a função de divisão retornou uma string de erro
                    print(f"--> {resultado}")
                else:
                    print(f"--> O poder foi dividido! O resultado é: {resultado}")
        else:
            print("\nMovimento inválido! Por favor, escolha uma opção da lista.")

# Inicia o programa
if __name__ == "__main__":
    calculadora_pokemon()