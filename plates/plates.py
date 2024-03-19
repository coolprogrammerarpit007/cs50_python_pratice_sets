import string

def main():
  plate = input("Plate: ")
  if(is_valid(plate)):
    print('Valid')
  else:
    print('Invalid')

def is_valid(plate):
  # To check if entered input is size required or not
  is_valid_length = is_valid_size(plate)

  if not(is_valid_length):
    return False
  else:
    # Check if plate must start with two letters
    start_with_letters = is_start_with_letters(plate)
    if(not(start_with_letters)):
      return False
    else:
      # check if word contains digits in middle of word
      middle_digit = is_middle_digit(plate)
      # print("middle_digit: ",middle_digit)
      if not(not(middle_digit)):
        return False
      else:
        # To check whether first number in word is 0 or not
        first_number_zero = is_first_number_zero(plate)
        if first_number_zero:
          return False
        else:
          # To check whether word contains puncuation or not
          is_punctuation = has_punctuation(plate)
          if is_punctuation:
            return False
          else:
            return True
    
  

# function to determine if entered input is of valid size or not

def is_valid_size(word):
  length = len(word)
  if length >= 2 and length <= 6:
    return True
  else:
    return False


# function to determine whether statrt with letters or not

def is_start_with_letters(word):
  letters = word[0:2]
  for letter in letters:
    if not(letter.isalpha()):
      return False
  return True


# function to check whether digits are in middle of a word or not

def is_middle_digit(word):
  # print(word)
  for i in range(len(word)-1):
    # to check if a digit is in middle if it is then return false
    
    if word[i].isdigit() and word[i+1].isalpha():
      # print('Middle digiit in word: ')
      return True
  return False

# function to chech whether first number is digit or not in python

def is_first_number_zero(word):
  contains_digit = False
  for char in word:
      if char.isdigit():
        contains_digit = True
        break

  if contains_digit:  
    numbers = []
    for i in word:
      if i.isdigit():
        numbers.append(int(i))
    return True if numbers[0] == 0 else False
  else:
    return False

# function to check whether a word contains punctuation or not

def has_punctuation(word):
  for char in word:
    if char in string.punctuation:
      return True
  return False

main()