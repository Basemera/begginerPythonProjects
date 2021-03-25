import random

def rock_paper_scissors():
    user = input("r for rock, p for paper s for scissors")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print(f"tie play again")
        rock_paper_scissors()
    elif user == 'r' and computer == 's':
        print(f"Rock crashes scissors you win")
    elif user == 'p' and computer == 's':
        print(f"scissors cut paper you lose")
    elif user == 's' and computer == 'r':
        print(f"Rock crashes scissors you lose")
    elif user == 's' and computer == 'p':
        print(f"scissors cut paper you win")
    elif user == 'r' and computer == 'p':
        print("Paper covers rock you lose")
    elif user == 'p' and computer == 'r':
        print("Paper covers rock you win")
    else:
        print("No right choice play again")
        rock_paper_scissors()

if __name__ == '__main__':
    rock_paper_scissors()
