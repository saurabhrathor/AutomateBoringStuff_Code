'''I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!'''

import random

print(" guess the correct no. between 1-20")

numb = random.randint(1,20)
for i in range(6):
	print("Left out attempts - ", 6-i)
	a = int(input())
	
	if a < numb:
		print('your guess is less than ans. Try again')
	elif a> numb:
		print('your guess is greater than ans. Try again')
	else:
		break;
		
if a == numb:
	print('Great, you got the answer', a)
else: 			
	print('Your attempts r over')
