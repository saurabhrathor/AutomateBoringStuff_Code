

def collatz(number):
	if number%2 == 0:
		return int(number//2)
	
	elif number%2 == 1:
		return int(3 * number +1)
	
def intInput():
	try:
		return int(input()) # Handle error if ValueError appears
	except ValueError:
		print('Enter an integer value')
	
print('Enter any number')
numb = intInput()
while numb==None:  ### Loop until you get an Integer
	numb = intInput()

while (numb > 1):
	numb = collatz(numb)
	print(numb)