"""
Exercícios de Revisão

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-26


----- Exercício 08 -----

# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já 
# tem a combinação de 5 cartas :)


5 Principais combinações consideradas
(https://www.pokerstars.com/br/poker/games/rules/hand-rankings/?no_redirect=1)

    1°) Royal Flush
    2°) Straight Flush
    3°) Quadra
    4°) Full House
    5°) Flush
"""

# Standard library imports
import sys
import os

# Importa classes descritas por Allen Downey (2015)
# em: https://penseallen.github.io/PensePython2e/18-heranca.html
from utils import poker_classes


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


def hand_classification(hand) -> bool:
    """Classifica a mão do jogador

    > Argumentos:
        - hand (Hand): Mão do jogador.
    
    > Output:
        - (str): Classificação da mão do jogador.
    """

    # Recupera cartas e naipes
    card_ranks = [x.rank for x in hand.cards]
    card_suits = [x.suit for x in hand.cards]

    max_card, min_card = max(card_ranks), min(card_ranks)
    num_suits = len(set(card_suits))
    unique_cards = len(set(card_ranks))
    
    # Royal Flush, Straight FLush e Flush
    if num_suits == 1:
        
        # Royal Flush
        if sorted(card_ranks) == [1, 10, 11, 12, 13]:
            return "Royal Flush"
        
        # Straight Flush
        elif sorted(card_ranks) == list(range(min_card, max_card+1)):
            return "Straight Flush"
        
        # Flush
        else:
            return "Flush"
    
    # Sequence
    elif sorted(card_ranks) == list(range(min_card, max_card+1)):
        return "Sequence"
    
    # Quadra ou Full House
    elif unique_cards == 2:

        # Recupera primeira carta
        x = card_ranks[0]
        counter = 1
        for i in card_ranks:
            if i == x:
                counter += 1

        # Quadra
        if counter == 4 or counter == 1:
            return "Quadra"
        
        # Full House
        else:
            return "Full House"
    
    # Dois pares ou uma trinca
    elif unique_cards == 3:

        # Dois pares

        # Trinca
        return "Two Pairs of One Three of a Kind"
    
    # Um par
    elif unique_cards == 4:
        return "One Pair"
    
    # Highest Card
    else:
        return "Highest card"
        

def main():
    """Realiza análise da mão do jogador

    > Argumentos:
        - Sem argumentos;
    
    > Output:
        - Sem output.
    """
    # Apresentação
    print("\n\n > CLASSIFICAÇÃO DA MÃO NO POKER!")
    print("\nClassifica a mão do jogador em uma rodade de poker\n")

    # Inicializa baralho e o embralha
    deck = poker_classes.Deck()
    deck.shuffle()

    # Inicializa mão do jogador 
    hand = poker_classes.Hand()

    # Move 5 cartas do baralho para compor a mão do jogador
    deck.move_cards(hand, 5)
    hand.sort()
    
    # Apresenta mão        
    print(hand)

    # Apresenta classificação da mão
    print(f"\nClassificação: {hand_classification(hand)}\n")


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
