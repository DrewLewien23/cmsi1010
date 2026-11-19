import sys
from card import (Card, standard_deck, shuffled_deck, deal_one_five_card_hand)

while True: 

  players = input("How many players today?! ")

  if str(players) == "bye" or str(players) == "exit":
    print("Goodbye!")
    sys.exit()
  if ((int(players)) > 2 and (int(players) < 10)):
    for i in range(int(players)):
      print(deal_one_five_card_hand())
  if int((int(players)) < 2 or (int(players) > 10)):
    print("That number isn't valid! Try again.")