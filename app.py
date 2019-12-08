from captchaSolver import getCaptcha

cont = 'y'
while cont == 'y':
	print("Enter the Image URL: ")
	url = input()
	print(getCaptcha(url))
	print("continue? (y/n)")
	cont = input()
