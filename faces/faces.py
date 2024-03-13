
def main():
  str = input('Enter: ');
  new_string = convert(str);
  print(new_string);


def convert(str):
  str = str.replace(':)','😊');
  str = str.replace(':(','😞');
  return str;




main();


