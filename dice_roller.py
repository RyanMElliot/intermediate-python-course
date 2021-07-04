def main():
  import random

  dice_size = int(input('How many sides do the dice have?'))
  dice_rolls = int(input('How many dice do you want to roll?'))
  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    if roll == 1:
      print(f'You rolled a {roll}! Sad times...')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Big win!')
    else:
      print(f'You rolled a {roll}')
    dice_sum = dice_sum + roll

  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()