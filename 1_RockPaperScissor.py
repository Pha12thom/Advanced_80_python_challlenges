from getpass import getpass as input

player1 = input("Player 1, choose R, P, or S: ")
player2 = input("Player 2, choose R, P, or S: ")

choices = ["R", "P", "S"]
while True:
    play = input("would you like to play again? (Y/N): ")
    if play == "Y":
        player1 = input("Player 1, choose R, P, S: ")
        player2 = input("Player 2, choose R, P, S: ")

        def userchoices(player1, player2):

            if player1 == "R" and player2 == "P":
                return "Player 2 wins"
            elif player1 == "R" and player2 == "S":
                return "Player 1 wins"
            elif player1 == "P" and player2 == "R":
                return "Player 1 wins"
            elif player1 == "P" and player2 == "S":
                return "Player 2 wins"
            elif player1 == "S" and player2 == "R":
                return "Player 2 wins"
            elif player1 == "S" and player2 == "P":
                return "Player 1 wins"
            else:
                return "It's a tie"

        print(userchoices(player1, player2))
    else:
        break
