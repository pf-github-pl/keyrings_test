import keyring
import getpass


def set_new_password():
	password = getpass.getpass("New password: ")
	password_rep = getpass.getpass("Repeat new password: ")
	if password != password_rep:
		print("Passwords do not match!! Please try again.")
		set_new_password()
	keyring.set_password('system', username, password)
	print("New user created.")


def validate(username):
	def wrapper(function):
		def inner_wrapper(*args, **kwargs):

			if keyring.get_password('system', username) == None:
				print("User does not exists! Please provide password to create new account. ")
				set_new_password()
				
			elif keyring.get_password('system', username) != None:
				password = getpass.getpass("Password: ")

				if password != keyring.get_password('system', username):
					print("Wrong password. Access Denied!")

				elif password == keyring.get_password('system', username):
					print(f"You are logged in now. It's nice to see you {username}!")
					return function(*args, **kwargs)

		return inner_wrapper

	return wrapper


username = input("Username: ")

@validate(username)
def print_secret():
	return print('*'*52, '* This is my secret message for logged in users ;) *', '*'*52, sep='\n')

print_secret()