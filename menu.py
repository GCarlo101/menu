import webbrowser

# Print the option menu
print('**********************************')
print('* select either 1 or 2           *')
print('* 1: order Domino\'s                 *')
print('* 2: order McDonald\'s           *')
print('**********************************')

# Get user choice
choice = input('Select 1 for Domino\'s or 2 for McDonald\'s: ')

while choice != '1' and choice != '2':
    print('You must either enter 1 or 2.')
    choice = input('Select 1 for Domino\'s or 2 for McDonald\'s: ')

# Convert the choice to an integer
choice = int(choice)

# Process the user's choice
if choice == 1:
    print('Processing option 1: Ordering Dominos')
    webbrowser.open("https://www.dominos.co.uk/")
elif choice == 2:
    print('Processing option 2: Ordering McDonald\'s')
    webbrowser.open("https://www.mcdonalds.com/gb/en-gb/menu.html")
