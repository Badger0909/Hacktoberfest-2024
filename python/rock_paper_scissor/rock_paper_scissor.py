print("What do you choose?\n type 0 for rock , type 1 for paper , type 2 for scissor ")
rock = """rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
your_choice = int(input())
if your_choice >=3 or your_choice < 0:
  print("You typed invalid number!")
else:
  print(game_images[your_choice])



  print("\nComputer's choice\n")
  import random
  com_choice = random.randint(0,2)
  if com_choice == 0:
    print(rock)
  elif com_choice == 1:
    print(paper)
  else:
    print(scissors)

  if your_choice == 0 and com_choice == 1 :
    print("\nYou lose")
  elif your_choice == 0 and com_choice == 2 :
    print("\nyou win")
  elif your_choice == 1 and com_choice == 0 :
    print("\nyou win")
  elif your_choice == 1 and com_choice == 2 :
    print("\nYou lose")
  elif your_choice == 2 and com_choice == 0 :
    print("\nYou lose")
  elif your_choice == 2 and com_choice == 1 :
    print("\nYou win")
  else:
    print("\nIts a Draw")