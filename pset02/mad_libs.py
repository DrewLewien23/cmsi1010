import random
import sys

while True:
  print("Welcome to madlibs! Please answer the questions and you will get three madlibs!")

  adjective = input("please enter an adjective ") 
  creature = input("please enter a creature ")
  weapon = input("please enter a weapon ")
  dessert = input("please enter a dessert ")
  adverb = input("please enter an adverb ")
  verb = input("please enter a verb ")
  noun = input("please enter a noun ")
  place = input("please enter a place ")

  if len(adjective or creature or weapon or dessert or adverb or verb or noun or place) > 30:
    print("too long!")
    sys.exit()

  templates = [
    {
      "text": f"A {adjective} ghost is behind you!", 
      "Written by": "rtoal"
    }, 
    {
      "text": f"Some {adjective} {creature} with a {weapon} is eating {dessert}",
      "Written by": "rtoal"
    },
    {
      "text": f"Look! There is a {adverb} {adjective} {verb} a {noun} in {place}",
      "Written by": "The whole class"
    }, 
    {
      "text": f"Watch out for the {creature}! It's headed towards {place}.", 
      "Written by": "drew" 
    }, 
    {
      "text": f"The {adjective} {weapon} killed the biiiig {creature}", 
      "Written by": "drew"
    },
    {
      "text": f"You ate {dessert} at {place}",
      "Written by": "drew"
    },
    {
      "text": f"Look at the {noun} that is lowkey {adjective}. Run! Do it {adverb}!",
      "Written by": "drew"
    },
    {
      "text": f"GET OUT OF THERE! IT'S A {creature}!!",
      "Written by": "drew"
    },
    {
      "text": f"That {place} is {adjective}",
      "Written by": "drew"
    },
    {
      "text": f"I bet you wish you got a madlib, didn't you?",
      "Written by": "drew"
    },
  ]

  for i in range(3):
    current_template = random.choice(templates)
    print(current_template) 

  print("")

  again = input("do you want to play again? ")

  yes_answers = {"yes", "si", "oui", "yup", "bet", "yep", "Y"}

  if again in yes_answers:
    print("")
    print("Playing again!")
  else: 
    print("Okay! Bye!")
    sys.exit()