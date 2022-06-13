import keyring
import getpass


def print_secret(validated:bool):
	if validated:
		return print('*'*52, '* This is my secret message for logged in users ;) *', '*'*52, sep='\n')


def set_new_password():
	password = getpass.getpass("New password: ")
	password_rep = getpass.getpass("Repeat new password: ")
	if password != password_rep:
		print("Passwords do not match!! Please try again.")
		set_new_password()
	keyring.set_password('system', username, password)
	print("New user created.")
	#return password


def validate(username):
	if keyring.get_password('system', username) == None:
		print("User does not exists! Please provide password to create new account. ")
		set_new_password()

	elif keyring.get_password('system', username) != None:
		password = getpass.getpass("Password: ")

		if password != keyring.get_password('system', username):
			print("Wrong password. Access Denied!")

		elif password == keyring.get_password('system', username):
			print(f"You are logged in now. It's nice to see you {username}!")
			return True


username = input("Username: ")

is_validated = validate(username)

print_secret(is_validated)