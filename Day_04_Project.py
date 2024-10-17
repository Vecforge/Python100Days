import random 

print("What do you choose? Type 0 for Rock, 1 for Papers or 2 for Scissors")
rps = int(input())

print("You chose: \n")
if rps == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif rps == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif rps == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

else:
    print("Not a valid option!")

c_rps = random.randrange(0, 3)

print("The computer chose: \n")
if c_rps == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif c_rps == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if rps == 0 and c_rps == 2:
    print("You won")

elif rps == 1 and c_rps == 0:
    print("You won")

elif rps == 2 and c_rps == 1:
    print("You won")

elif rps == 0 and c_rps == 1:
    print("You lost")

elif rps == 1 and c_rps == 2:
    print("You lost")

elif rps == 2 and c_rps == 3:
    print("You lost")

else:
    print("It's a tie")