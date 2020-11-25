"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-25


----- Exercício 02 -----

# Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os
#        respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta 
#       seja menor. Acrescente 10% de folga e sempre arredonde os 
#       valores para cima, isto é, considere latas cheias.

"""

# Standard library imports
import sys
import os

# Redimento de litros por metro quadrado
REND_TINTA = 1/6

# Preço unitario das latas
PRECOS = {"18": 80, "3.6": 25}


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
    # Capta area a ser pintada
    print("\n\n > CONSULTA LOJA DE TINTAS!")
    print(f"\n---- ÁREA A SER PINTADA\n")
    area = read_float_pos("Área a ser pintada (m²): ")
    
    # Calcula quantidade de tinta e adiciona margem de 10%
    qtd_tinta = (area*REND_TINTA)*1.1

    # Apresenta cabeçalho
    print("\n" + "*"*60)
    print(f"{' LATAS DE TINTA ':^60}")
    print("*"*60 + "\n")

    # Apresenta resumo
    print(f"> Área: {area} m²")
    print(f"> Rendimento: {REND_TINTA:.4f} L/m²".replace(".", ","))
    print(f"> Litros de tinta necessários: {qtd_tinta:.2f} L".replace(".", ","))

    # Apresenta quantidade de latas de 18 L
    print("\n  > Apenas latas de 18 litros:")
    latas = int((qtd_tinta//18)+1)
    print(f"      - {latas} Latas")
    print(f"      - R$ {latas*PRECOS['18']:.2f}".replace(".", ","))

    # Apresenta quantidade de latas de 3,6 L
    print("\n  > Apenas latas de 3,6 litros:")
    latas = int((qtd_tinta//3.6)+1)
    print(f"      - {latas} Latas")
    print(f"      - R$ {latas*PRECOS['3.6']:.2f}".replace(".", ","))

    # Apresenta quantidade de latas de 18 e 3,6 L
    print("\n  > Latas de 18 e 3,6 litros:")
    latas_18 = qtd_tinta//18
    qtd_tinta -= latas_18*18
    latas_3_6 = qtd_tinta//3.6 + 1
    print(f"      - {int(latas_18)} Latas de 18 L")
    print(f"      - {int(latas_3_6)} Latas de 3,6 L")
    preco = latas_18*PRECOS['18'] + latas_3_6*PRECOS['3.6']
    print(f"      - R$ {preco:.2f}".replace(".", ","))
    
    # Apresenta rodapé
    print("\n" + "*"*60 + "\n")

if __name__ == "__main__":

    # Executa aplicação
    while True:
        
        # Executa rotina
        main()

        # Verifica se usuário deseja executar nova rodada
        while True:

            # Capta resposta do usuário
            res = input("Realizar nova consulta?! [(s)/n]").strip().lower()

            # Teste se input é válido
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


