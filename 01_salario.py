"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-25


----- Exercício 01 -----

Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% para o Imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

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
            sys.exit("\nSaindo, até logo! ...\n")
        
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
    # Realiza leitura de salário e horas trabalhadas
    print("\n\n > IMPOSTOS SOBRE SALÁRIO!")
    print(f"\n---- LEITURA DE DADOS\n")
    sal_hora = read_float_pos("Qual o seu salário por hora (R$/h)? ")
    horas = read_float_pos("Quantas horas você trabalhou no último mês? ")
    salario = sal_hora*horas
    
    # Apresenta cabeçalho
    print("\n" + "*"*60)
    print(f"{' DEDUÇÕES DE IMPOSTOS ':^60}")
    print("*"*60 + "\n")
    
    # Apresenta informações
    print(f"  + Salário Bruto: R$ {salario:.2f}".replace(".", ","))
    print(f"  - IR (11%): R$ {salario*0.11:.2f}".replace(".", ","))
    print(f"  - INSS (8%): R$ {salario*0.08:.2f}".replace(".", ","))
    print(f"  - Sindicato (5%): R$ {salario*0.05:.2f}".replace(".", ","))
    print(f"\n  = Salário Líquido: R$ {salario*0.77:.2f}".replace(".", ","))

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
