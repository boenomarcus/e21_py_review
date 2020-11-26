"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-26


----- Exercício 03 -----

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
# isósceles ou escaleno. 

"""

# Standard library imports
import sys
import os


def read_float_pos(txt:str) -> float:
    """Realiza leitura de valor real positivo

    > Argumentos:
        - txt (str): Texto para input.
    
    > Output:
        - (float): Valor real indicado pelo usuário
    """

    # Capta salário por hora
    while True:

        # Realiza leitura do salário
        try:
            f = float(input(txt))
        
        # Sai do sistema com a interrupção
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo! ...\n")
        
        # Indica erro de tipo
        except ValueError:
            print("[ERRO] Valor inválido, digite novamente!")
        else:
            # Testa domínio
            if f > 0:
                return f
            print("[ERRO] Valor inválido, digite novamente!")


def limpar_tela():
    """Limpeza da tela

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada execução
    # "cls" para windows e "clear" para linux/mac (posix)
    os.system('cls') if os.name == 'nt' else os.system('clear')


def main():
    """

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """

    # Apresentação
    print("\n\n > CONSTRUÇÃO DE TRIÂNGULOS!")
    print(f"\n---- LADOS DO TRIÂNGULO\n")

    # Realiza leitura dos lados de possivel trinangulo
    l = [read_float_pos(f"Lado {x+1}: ") for x in range(3)]

    # Testa condições para ser um triângulo
    c1 = abs(l[1] - l[2]) < l[0] < l[1] + l[2]
    c2 = abs(l[0] - l[2]) < l[1] < l[0] + l[2]
    c3 = abs(l[0] - l[1]) < l[2] < l[0] + l[1]

    # Identifica se lados formam um triângulo
    if c1 and c2 and c3:
        
        # Triângulo equilátero
        if l[0] == l[1] == l[2]:
            print("\nTriângulo equilátero (todos lados iguais)\n")
        
        # Triângulo isósceles
        elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
            print("\nTriângulo isósceles (2 lados iguais)\n")
        
        # Triângulo escaleno
        else:
            print("\nTriângulo escaleno (todos lados diferentes)\n")

    # Indica que os lados não formam um triângulo
    else:
        print("\nOs lados NÃO formam um triângulo!\n")
    

if __name__ == "__main__":

    # Executa aplicação
    while True:
        
        # Executa rotina
        main()

        # Verifica se usuário deseja executar nova rodada
        while True:

            # Capta resposta do usuário
            try:
                res = input("Realizar nova consulta?! [(s)/n] ").strip().lower()
            
            # Sai do sistema
            except KeyboardInterrupt:
                sys.exit("\n\nSaindo, até logo! ...\n")
            
            # Teste se input é válido
            else:
                if res in "sn":
                    break
                print("[ERRO] Digite 's' para continuar ou 'n' para sair!")
            
        # Verifica se usuario deseja terminar execução
        if res == "n":
            break

        # Limpar terminal para nova execução
        limpar_tela()
    
    # Indica saída do sistema
    print("\nSaindo, até logo! ...\n")
