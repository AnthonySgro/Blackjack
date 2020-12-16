import random
import os


def cls():
    """Clears console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate_score(hand):
    """Calculates scores"""
    # if Blackjack, return 0 so we know
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    # if over 21, make sure aces count as 1
    elif sum(hand) > 21:
        for card in range(0, len(hand)):
            if hand[card] == 11:
                hand[card] = 1
    return sum(hand)


def deal_card():
    """Deals a single card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user_cards, user_score, computer_score, wins, losses, draws):
    """Decides winning output and calculates record"""
    if user_score == 0 and computer_score == 0:
        wins += 1
        print("🤩 Wow! Double Blackjack. House rules say you win.")
    elif user_score == 0:
        wins += 1
        print("👌😤 You got Blackjack!. You win!")
    elif user_score > 21:
        losses += 1
        print("😩 User busts. You lose.")
    elif len(user_cards) > 4:
        wins += 1
        print(
            f"🥳 You have {len(user_cards)} cards and haven't busted! You win.")
    elif computer_score == 0:
        losses += 1
        print("🤬 Computer has Blackjack! You lose.")
    elif user_score == computer_score:
        draws += 1
        print("😒 It's a draw.")
    elif computer_score > 21:
        wins += 1
        print("🥳 Computer busts. You win!")
    elif user_score > computer_score:
        wins += 1
        print("😄 User score is higher. You win!")
    elif computer_score > user_score:
        losses += 1
        print("😩 Computer score is higher. You lose.")
    print(f"Current record: ({wins}-{losses}-{draws})")
    return True, wins, losses, draws


def print_results(user_cards, computer_cards):
    """Prints final scores and cards on victory"""
    print("----------------------------\n")

    if calculate_score(user_cards) == 0:
        # If Blackjack, change palceholder to 21
        print(
            f"Your final hand: {user_cards}, final score: 21")
    else:
        print(
            f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")

    if calculate_score(computer_cards) == 0:
        print(
            # If Blackjack, change  palceholder to 21
            f"Computer's final hand: {computer_cards}, final score: 21")
    else:
        print(
            f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    return


def play_again():
    """Asks user to replay game."""
    another_game = input("\nDo you want to play again? Type 'y' or 'n': ")
    if another_game == 'n':
        return 0
    elif another_game == 'y':
        return 1
    else:
        print("Send valid input.")
        return 2


def init(wins, losses, draws):
    """Initializes Blackjack"""
    cls()
    print("Welcome to Anthony's Blackjack table.")
    print("----------------------------\n")

    user_cards = []
    computer_cards = []
    end_game = False

    # Deal out two cards to each player
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    # Put game in a while loop so we
    # can end whenever somebody wins.
    while not end_game:
        if calculate_score(user_cards) == 0:
            print(f"Your score: 21")
        else:
            print(f"Your score: {calculate_score(user_cards)}")
        print(f"Your hand: {user_cards}")
        print(f"Dealer's first card: {computer_cards[0]}")

        # Check if you got blackjack.
        if calculate_score(user_cards) == 0:
            end_game = True

        # It's the user's turn
        user_turn = True
        while user_turn:
            new_card = input(
                "Do you want to draw another card? Press 'y' or 'n': ")

            # User wants card, loop this
            if new_card == 'y':
                user_cards.append(deal_card())
                print("----------------------------\n")
                print(f"Your score: {calculate_score(user_cards)}")
                print(f"Your hand: {user_cards}")

                # If user busts, end loop
                if calculate_score(user_cards) > 21:
                    user_turn = False

            # User doesn't want card, break loop
            elif new_card == 'n':
                user_turn = False

            # Disgruntled user...
            elif new_card != 'n' and new_card != 'y':
                print("Enter valid input.")

            # Check for 5 card rule
            if len(user_cards) == 5:
                user_turn = False

        # Computer's draws if score less than 17, if they dont have blackjack, if the human hasn't busted, if the human doesn't have blackjack, and if the human doesn't have 5 cards)
        while calculate_score(computer_cards) < 17 and not calculate_score(computer_cards) == 0 and not calculate_score(user_cards) > 21 and not calculate_score(user_cards) == 0 and len(user_cards) != 5:
            computer_cards.append(deal_card())

        print_results(user_cards, computer_cards)

        # Show end results
        end_game, wins, losses, draws = compare(user_cards, calculate_score(
            user_cards), calculate_score(computer_cards), wins, losses, draws)

    # Ask to play again. If nonsensical answer,
    # keep asking for 'y' or 'n'
    another_game = play_again()
    while another_game == 2:
        another_game = play_again()

    # if given valid response...
    if another_game == 1:

        # Play again
        cls()
        init(wins, losses, draws)

    elif another_game == 0:

        # Print results and goodbye messages
        cls()
        print(f"Final record: {wins}-{losses}-{draws}")
        win_percentage = round(100 * (2 * wins + draws) /
                               (2 * (wins + losses + draws)), 2)
        print(f"Win Rate: {win_percentage}%")
        if win_percentage < 50:
            print("The house beat you. Better luck next time. Goodbye!")
        elif win_percentage > 50:
            print("You beat the house! Nice work. Goodbye!")
        elif win_percentage == 50:
            print("Wow, a dead heat! What are the odds. Goodbye!")


def begin():
    """Welcome dialogue."""
    wins = 0
    losses = 0
    draws = 0
    want_to_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if want_to_play == 'y':
        init(wins, losses, draws)
    elif want_to_play == 'n':
        print("\nOkay, have a nice day.")
    else:
        cls()
        print("\nSend valid input.")
        begin()


cls()
begin()
