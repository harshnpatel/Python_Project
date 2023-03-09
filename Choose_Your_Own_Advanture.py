name = input("Enter the name ")
print("Welcome", name, "to this advanture! ")

answer = input("You are on a dirt road, it has come to end and you can go left or right,Which way you want to go?").lower()

if answer == "left":
    answer = input("You come to river,you can walk around it or swim accross? Type walk to walk around swim to swim across (swim/walk) ? : ").lower()

    if answer == "swim":
        print("You swim accross and waee eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles,ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge,it looks wobbly, do you want to cross it or hesd back (cross/back)? ").lower()

    if answer == "back":
        print("You go back or lose.")
    elif answer == "cross":
        answer == input("You cross the bridge and meet the stranger, Do you want to talk (Yes/No)").lower()

        if answer == "yes":
            print("you talk to the stranger and you got an Gold and you win! ")
        elif answer == "no":
            print("You ignore the stranger and the are offerended and then you lose ")
        else:
            print("Not a valid option. You lose.")
        
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying ",name)