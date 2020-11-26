"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-26


----- Exercício 07 -----

# Conta espaços e vogais. Dado uma string com uma frase informada pelo 
# usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

"""

# Standard library imports
import sys
import os


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
    print("\n\n > CONTAGEM DE CARACTERES!")
    print("\nContagem de caracteres e espaços em branco em uma frase\n")
    
    # Leitura do valor limite
    frase = input("Digite uma frase:\n")

    # Realiza contagem de vogais e espaços em branco
    vogais = {"a":0, "e":0, "i":0, "o":0, "u":0}
    vogais_total, branco = 0, 0
    for caracter in frase:
        if caracter.lower() in ["a", "e", "i", "o", "u"]:
            vogais_total += 1
            vogais[caracter.lower()] += 1
        elif caracter == " ":
            branco += 1
    
    # Apresenta cabeçalho
    print("\n" + "*"*40)
    print(f"{' CONTAGEM DE CARACTERES ':^40}")
    print("*"*40 + "\n")

    # Apresenta contagem
    print(f"\n# de Vogais: {vogais_total}")
    for vogal in vogais.items():
        print(f"    > # de {vogal[0].upper()}'s: {vogal[1]}")
    print(f"\n# de espaços em branco: {branco}\n")

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
