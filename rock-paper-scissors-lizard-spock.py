import random 

def name_to_number(name):
  num = None 
  if name == 'rock':
    num = 0 
  elif name == 'Spock':
    num = 1
  elif name == 'paper':
    num = 2
  elif name == 'lizard':
    num = 3
  elif name == 'scissors':
    num = 4
  else:
    num = "uh oh! ERRORRRRRR MESSAGE"
  return num

def number_to_name(number):
  name = None 
  if number == 0:
    name = 'rock' 
  elif number == 1:
    name = 'Spock'
  elif number == 2:
    name = 'paper'
  elif number == 3:
    name = 'lizard'
  elif number == 4:
    name = 'scissors'
  else:
    name = "uh oh! ERRORRRRRR MESSAGE"
  return name
  
def rpsls(player_choice): 
    user_guess_num = name_to_number(player_choice)
    computer_guess_num = random.randrange(0, 5)
    computer_guess_name = number_to_name(computer_guess_num)

    if user_guess_num - computer_guess_num == 0:
        print "You both picked", number_to_name(computer_guess_num), "you have tied!"
    elif user_guess_num - computer_guess_num != 0:
        print "Player chooses", player_choice, "\n","Computer chooses", computer_guess_name
        if ((user_guess_num - computer_guess_num) % 5) > 2:
            print "Computer wins! \n"
        else:
            print "Player wins! \n"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

