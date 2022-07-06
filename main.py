import random

print("...rock...")
print("...paper...")
print("...scissors...")
player = input("enter your choice: ").strip().lower()


computer = random.randint(1,3)

if computer == 1:
  computer = "rock"
elif computer == 2:
  computer= "scissors"
else:
  computer = "paper"

print(f"computer chose {computer}")
if player == computer:
	print("Its a tie!")

elif player == "rock":
	if computer == "scissors":
		print("rock beats scissors, Player 1 wins")
	elif computer == "paper":
		print("paper covers rock, player 2 wins")

elif player == "scissors":
	if computer == "paper":
		print("scissors cuts paper, player 1 wins")
	if computer == "rock":
		print("rock smashes scissors, player 2 wins")

elif player == "paper":
	if computer == "rock":
		print("paper covers rock, player 1 wins")
	if computer == "scissors":
		print("scissors cuts paper, player 2 wins")

else:
	print("Something went wrong")
