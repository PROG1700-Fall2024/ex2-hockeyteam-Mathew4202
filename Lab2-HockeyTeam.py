# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

"""
Student Name:    Mathew Akunyili
Program Title:  Hockey Team
Description:    calculate the win percentage of an hockey team the user gives
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Welcome user to program
    print("Hey welcome to our peogram which helps you calculate the win percentge of any team")

    #Ask user for the hockey team
    Team = input("Please enter the name of your hockey team")

    #Ask user how many wins the team has
    Wins = int(input("How many wins does " + str(Team) + " has"))

    #Ask user how many losses the team has
    Losses = int(input("How many Loss does " + str(Team) + " has"))

    #Calcuations
    Games = Wins + Losses
    Percentage = 100*(Wins/Games)
    formatPercentage = "{:.4f}".format(Percentage)
    print("The " + Team + " has " + str(Wins) + " wins and " + str(Losses) + " losses, with a win percentage of " + str(formatPercentage) + ".")
    

    #Thankyou message
    print("Thanks for using our program to calculate the percentage of your hockey team, hope we see you soon")








    # YOUR CODE ENDS HERE

main()