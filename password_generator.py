#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
char_counts = [nr_letters, nr_numbers, nr_symbols] # Total number of characters left to use
categories = [letters, numbers, symbols]

# Check if we have characters left to use

while sum(char_counts) > 0:

  # Use random to select what kind of character we use: letter, number or symbol
  category = random.randint(0, 2)
  
  # Check if the randomly picked category has elements left for being metioned
  if char_counts[category] > 0:
    
    # Use random to select the character from the already established category
    #character = random.randint(0, len(categories[category])-1) or more elegant:
    character = random.choice(categories[category])
     
    # Append the character to the password
    password.append(character)
    
    # Reduce the nubmer of characters by 1 from the respective category: nr_letters, nr_symbols and nr_numbers
    char_counts[category] -= 1
    
# Transform password to string and print it
final_password = ''.join(password)
print(f"Your password is {final_password}")
