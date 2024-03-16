
string = input('camelCase: ');
newString = '';


for letter in string:
  if letter.isupper():   # check if letter is in upper case or not
    newString = newString + '_' + letter; # Add _ to the string
  else:
    newString = newString + letter; #Else add characters as it ease.

print(f"snake_case: {newString.lower()}");


