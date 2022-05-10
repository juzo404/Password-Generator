import string
import random


## Characters from which we will generate the password
characters = list (string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():

	## Setting the password lenght by the user
	length = int(input("Enter password length: "))

	## Shuffle characters
	random.shuffle(characters)
	
	## We retrieve random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## Shuffle password
	random.shuffle(password)

	## We convert the list into a string
	## Then we display
	print("".join(password))



## Finally we call the function
generate_random_password()
