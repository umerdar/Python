#make a list to hold onto out items
shopping_list = []

# print out instructions on how to use the app
def menu():
	print("What should we pick up at the store?")
	print("Enter 'DONE' to stop adding items.")
	print("Enter 'SHOW' to show all the items on the list")
	print("Enter 'HELP' to show the menu.")

menu()


while True:
	# ask for new items
	new_item = input("> ")

	# be able to to quit the app
	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		menu()
		continue

	# add new items to out list
	shopping_list.append(new_item)

# print out the list
print("Here's your list:")

for item in shopping_list:
	print(item)
