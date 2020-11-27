"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-26


----- Exercício 05 -----

# Faça um programa que simule um lançamento de dados. Lance o dado 100 
# vezes e armazene os resultados em um vetor. Depois, mostre quantas 
# vezes cada valor foi conseguido. Dica: use um vetor de contadores 
# (1-6) e uma função para gerar numeros aleatórios, simulando os 
# lançamentos dos dados.

"""

# Standard library imports
import sys
import os
import random


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


def main():
    """Menu principal

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresentação
    print("\n\n > LANÇAMENTO DE DADO!")
    print("\nLança dado n vezes e realiza contagem de números\n")
    
    # Leitura do valor limite
    n = read_int_pos("Quantas vezes deseja lançar o dado? ")

    # Dicionário para contagem do numero de vezes que cada valor foi sorteado
    contagem = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    # Realiza lançamento de dados
    for i in range(n):
        contagem[random.randint(1, 6)] += 1
    
    # Apresenta cabeçalho
    print("\n" + "*"*40)
    print(f"{' LANÇAMENTO DE DADOS ':^40}")
    print("*"*40 + "\n")

    # Apresenta contagem de valores
    print(f"\n> Dado lançado {n} vezes!\n")
    for valor in contagem.items():
        print(f"   > Face {valor[0]}: {valor[1]} vezes")
    
    # Apresenta rodapé
    print("\n" + "*"*40 + "\n")    
    

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
          
          
  #Cara você é muito bom mesmo! Algumas funções consegui entender aqui e percebi que elas facilitam muito nossa vida.
   # Teus códigos são sempre bem organizados e tu busca pensar em todas as falhas possíveis pra arrumar, muito legao isso.
