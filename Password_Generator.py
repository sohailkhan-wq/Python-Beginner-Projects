import random

characters_list = ['1','2','3','4','5','6','7','8','9','@', '$', '&', '~', '*', '(', ')', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'A', 'B', 'C', 'D', 'E', 'F',
'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user_requirements = int(input("Enter the number of your password characters: "))
password = random.choices(characters_list, k= user_requirements)
print("Here is your Password: " + ''.join(password))