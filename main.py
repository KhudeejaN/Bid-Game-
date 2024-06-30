


art = '''
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ '''





 
from replit import clear 

game_end = False

print(art + "Welcome to the auction of the year! ")
auction_game = []
while not game_end: # or while True 
  game_dictionary = {}
  game_play = input("Would you like to bid? Type y for yes or n for no.")
  if game_play == "n" or game_play == "no":
    print("Thank you for visiting the auction of the year")
  if game_play == "y" or game_play == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    game_dictionary["name"] = name 
    game_dictionary["bid"] = bid
    auction_game.append(game_dictionary)
    new_bidder = input("Is there another bidder? Type y for yes or n for no.")
    if new_bidder == "n" or new_bidder == "no":
      game_end = True
    clear()
  else:
    print("Please enter a valid input.")
  clear()


highest_bid = 0 
winner = ""
for num in auction_game:
  if num["bid"] > (highest_bid):
    highest_bid = num["bid"]
    winner = num["name"]
print(f"Winner is {winner} with a bid of {highest_bid}")
      


   
    
  




