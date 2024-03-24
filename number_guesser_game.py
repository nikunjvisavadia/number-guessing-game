import random

print("Welcome to Number Guessing Game !!")
print("""
      Instructions :
      You will asked for a number which will be the maximum number for the guessing.
      Once you will enter the number you will be asked to guess the number
      If the number you entered will be less than the number it will show "You are below the number"
      And if the number entered is greater than the actual number than it will show "You are above the number"
      """)

max_number = input("Enter a Number : ")

if max_number.isalpha():
      print('Please enter a number.')
      quit()
else:
      if max_number.isdigit() == False:
            print('Please type a number greater than 0.')
            quit()

answer = random.randint(0, int(max_number))

count = 0

while True:
      count +=1
      guess = input("Make a guess: ")
      
      if guess.isalpha():
            print('Please enter a number.')
      else:
            guess=int(guess)
      
      
      if guess == answer:
            print("You Won!!")
            break
      elif guess > answer:
            print("You are above the number")
      else:
            print("You are below the number")
            
print(f"You got the answer in {count} guesses")