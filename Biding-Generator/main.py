from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
keepLoop = "yes"
bidders_list = {}
while keepLoop == "yes":
  name = input("What is your name?: ")
  cash = int(input("What is your bid?: $"))
  bidders_list[name] = cash
  keepLoop = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if keepLoop == "yes":
    clear()

max = -1
winner = ""
for key in bidders_list:
  if bidders_list[key] > max:
    winner = key
    max = bidders_list[key]

print(f"The winner is {winner} with a bid of ${bidders_list[winner]}")

