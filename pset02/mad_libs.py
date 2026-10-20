# ---------------------------------------------------------------------
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------

import random
import sys

adjective = input("enter adjective ") 
creature = input("enter creature ")
weapon = input("enter weapon ")
dessert = input("enter dessert ")
adverb = input("enter adverb ")
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
    "text": f"Some {adjective} :creature with a :weapon is eating {dessert}",
    "Written by": "rtoal"
  },
  {
    "text": f"Look! There is a {adverb} {adjective} {verb} a {noun} in {place}",
    "Written by": "The whole class"
  }
]

yes_answers = {"yes", "si", "oui", "yup", "bet", "yep", "Y"}

current_template = random.choice(templates)

print(current_template)
print("")

again = input("do you want to play again? ")

if again in yes_answers:
  print("play again")
else: 
  print("Okay! Bye!")
  sys.exit()