try:
	count = int(input("give me a number: "))
except NameError:
	print("That's not a number!")
else:
	print("Hi " * count) 