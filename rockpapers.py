import random
computer = "Not selected"
def game(choice):
	global computer
	computer_brain = ["Rock", "Paper", "Scissor"]
	computer = random.choice(computer_brain)

	if choice == "A" and computer == "Paper" or choice == "B" and computer == "Scissor" or choice == "C" and computer == "Rock":
		return "lost", computer

	elif choice == "A" and computer == "Scissor" or choice == "B" and computer == "Rock" or choice == "C" and computer == "Paper":
		return "won", computer

	elif choice == "A" and computer == "Rock" or choice == "B" and computer == "Paper" or choice == "C" and computer == "Scissor":
		return "tie", computer

