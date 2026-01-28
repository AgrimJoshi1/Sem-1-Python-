import random
sec_num = random.randint(1,10)
guess_count = 1 
while guess_count <= 3: 
    guess = int(input("Take a guess between 1 and 10: "))
    guess_count+=1 
    if guess == sec_num:
        print("This is the correct guess!!!!!!!")
        break
    else: 
        print("Try again")
else: 
    print("You failed.")
    print(f"The number was {guess_count}")

