import random


def shuffle_shoe(n_decks=8):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = cards * 4
    shoe = deck * n_decks
    random.shuffle(shoe)
    return shoe


def deal_game(shoe):

    # initialize a list to store cards for player and banker
    player = []
    banker = []

    # define a card converter function
    def card_converter(card):
        return 10 if card in ['J', 'Q', 'K'] else card

    # deal the first four cards
    card1 = shoe.pop()
    card2 = shoe.pop()
    card3 = shoe.pop()
    card4 = shoe.pop()

    player.append(card_converter(card1))
    banker.append(card_converter(card2))
    player.append(card_converter(card3))
    banker.append(card_converter(card4))

    # test for player and banker pairs
    if card1 == card3:
        player_pair = 1
    else:
        player_pair = 0

    if card2 == card4:
        banker_pair = 1
    else:
        banker_pair = 0

    # calculate the player score
    player_score = sum(player) % 10
    banker_score = sum(banker) % 10

    # If either the player or banker is dealt a total of eight or nine,
    # both the player and banker stand (i.e. a "Natural"). This rule
    # overrules all others.
    if player_score >= 8 or banker_score >= 8:

        result = {'player': sum(player) % 10,
                  'banker': sum(banker) % 10,
                  'player_pair': player_pair,
                  'banker_pair': banker_pair}
        return result

    # If player has 6 or 7, he stands. Banker stands
    # if he also has 6 or 7.
    elif player_score >= 6 and banker_score >= 6:

        result = {'player': sum(player) % 10,
                  'banker': sum(banker) % 10,
                  'player_pair': player_pair,
                  'banker_pair': banker_pair}
        return result
    # If a player stands, the banker can only draw a hand
    # with a score of 5 and below.
    elif player_score >= 6 and banker_score <= 5:

        banker.append(card_converter(shoe.pop()))

    # If the player_score is <=5 he draws another card.
    elif player_score <= 5:

        player_draw = card_converter(shoe.pop())
        player.append(player_draw)

        # If banker's first 2 hands totals <= 2, draw a card.
        if banker_score <= 2:

            banker.append(card_converter(shoe.pop()))

        # If banker's first two cards totals 3 and if player_draw
        # is in [1,2,3,4,5,6,7,9,10] banker draws.
        elif banker_score == 3 and player_draw in [1, 2, 3, 4, 5, 6, 7, 9, 10]:

            banker.append(card_converter(shoe.pop()))

        # If banker's first two cards totals 4 and if player_draw
        # is in [2,3,4,5,6,7] banker draws.
        elif banker_score == 4 and player_draw in [2, 3, 4, 5, 6, 7]:

            banker.append(card_converter(shoe.pop()))

        # If banker's first two cards totals 5 and if player_draw
        # is in [4,5,6,7] banker draws.
        elif banker_score == 5 and player_draw in [4, 5, 6, 7]:

            banker.append(card_converter(shoe.pop()))

        # If banker's first two cards totals 6 and if player_draw
        # is in [6,7] banker draws.
        elif banker_score == 6 and player_draw in [6, 7]:

            banker.append(card_converter(shoe.pop()))

        # If banker score is 7 then he stands.
        elif banker_score == 7:
            pass

    result = {'player': sum(player) % 10,
              'banker': sum(banker) % 10,
              'player_card': player,
              'banker_card': banker,
              'player_pair': player_pair,
              'banker_pair': banker_pair}

    return result


def simulator(number_shoe=10):

    player_wins = 0
    banker_wins = 0
    ties = 0

    while number_shoe > 0:
        shoe = shuffle_shoe()

        while len(shoe) > 10:
            result = deal_game(shoe)
            if result['player'] > result['banker']:
                player_wins += 1
            elif result['player'] < result['banker']:
                banker_wins += 1
            else:
                ties += 1
        number_shoe -= 1
    total = player_wins + banker_wins + ties
    return player_wins / total, banker_wins / total, ties / total


if __name__ == '__main__':
    import sys
    n_shoes = int(sys.argv[1])
    print(simulator(number_shoe=n_shoes))
