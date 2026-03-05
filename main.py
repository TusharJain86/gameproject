computer= -1
youstr= input("Enter your choice: ")

youDict= {
    "s":1,
    "w":-1,
    "g":0
}

you = youDict[youstr]

if(computer == -1 and you ==1):
    print("You win!")

elif(computer == -1 and you == 0):
    print("Computer wins! Try again.")

elif(computer == 1 and you == -1):
    print("Computer wins! Try again.")

elif(computer == 1 and you == 0):
    print("You win!")

elif(computer == 0 and you == -1):
    print("Computer wins! Try again.")

elif(computer == 0 and you == 1):
    print("You win!")

else:    print("It's a tie! Try again or something went wrong.")