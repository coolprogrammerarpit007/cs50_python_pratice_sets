# time = input('Enter Time: ');
# hrs,mins = time.split(':');
# print(hrs)
# print(mins)

def main():
  time = input('Time: ');
  meal_time = convert(time);
  if(7<= meal_time <= 8):
    print('breakfast time');
  elif(12<= meal_time <= 13):
    print('lunch time');
  elif(18<= meal_time <= 19):
    print('dinner time');
  else:
    print('');


def convert(time):
  hrs,mins = time.split(':');
  hrs = float(hrs);
  mins = float(mins);
  return hrs + mins/60;

if __name__ == '__main__':
  main();