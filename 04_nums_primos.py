"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-26


----- Exercício 04 -----

# Faça um programa que gera uma lista dos números primos existentes 
# entre 1 e um número inteiro informado pelo usuário. 

"""

# Standard library imports
import sys
import os


def read_int_pos(txt:str) -> int:
    """Realiza leitura de valor inteiro positivo

    > Argumentos:
        - txt (str): Texto para input.
    
    > Output:
        - (int): Valor inteiro indicado pelo usuário
    """

    # Capta salário por hora
    while True:

        # Realiza leitura do salário
        try:
            f = int(input(txt))
        
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


def nums_primos(beg:int, end:int) -> list:
    """Computa números primos do intervalo

    > Argumentos:
        - beg (int): Valor inicial do intervalo;
        - end (int): Valor final do intervalo (inclusive).
    
    > Output:
        - (list): Lista de números primos dentro do intervalo indicado.
    """
    # Cria lista vazia para armazenar numeros primos
    nums = []

    # Itera sobre intervalo indicado
    for i in range(beg, end+1):

        # Inicializa soma e loop interno
        c, j = 0, 1
        while j <= i:
            # Se número for divisivel, incrementa o contador c
            if i%j == 0:
                c += 1
            j += 1
        
        # Se valor for divisível apenas por 1 e por ele mesmo, é primo
        if c <= 2:
            nums.append(i)
    
    # Retorna lista com números primos
    return nums


def main():
    """

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """

    # Apresentação
    print("\n\n > NÚMERO PRIMOS!")
    print("\nApresenta números primos entre 1 e um valor informado\n")
    
    # Leitura do valor limite
    lim = read_int_pos("Limite para série de números primos: ")

    # Recupera numeros primos entre intervalo indicado
    primos = nums_primos(1, lim)

    # Apresenta números primos em tela
    print(f"\n> Número primos entre 1 e {lim}:")
    print(f"      - {primos}\n")
    

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
    
    
    # Não entendi muita coisa mas acho que entendi sua lógica. Acho muito legal ver que várias lógicas podem resolver um exercício só.
    # Bem legal sua organização, Marcus
