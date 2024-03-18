# Incomplete program

def main():
  plate = input("Plate: ")
  if(is_valid(plate)):
    print('Valid')
  else:
    print('Invalid')

def is_valid(plate):
  # Writing my code here
  flag = True
  length = len(plate)
  if length <2 or length > 6:
    print('It Prints1')
    return False
  else:
    # Check if first two characters of plate are characters or not
    letters = plate[0:2]
    for letter in letters:
      if not(letter.isalpha()): # will check is letter is character or not
        flag = False  
      return flag

    # check if number is used in middle of the plate
    if is_alpha_numeric(plate):
      return False
    else:
      True
main()