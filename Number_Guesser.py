import random

top_of_range = input("Type the number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter the largeer then number than Zero next time ")
        quit()
else:
    print("Please Enter the largeer then number than Zero next time ")
    quit()


random_number = random.randint(0,top_of_range)
guesse_time = 0
print(random_number)

while True:
    guesse_time += 1
    User = input("Make a Guess: ")
    if User.isdigit():
        User = int(User)
    else:
        print("Please type the number the number next time")
        continue
    
    if User == random_number:
        print("You got it! ")
        break
    elif guesse_time > random_number:
        print("You were above the number!")
    else: 
        print("You were below the number!")
        
print("You got it in",guesse_time,"guesses")