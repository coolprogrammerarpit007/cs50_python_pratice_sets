
greetiing = input('Greeting: ').lower();
amount = 0;
if greetiing.startswith('hello'):
  amount = 0;
  print(f"${amount}");
elif greetiing.startswith('h'):
  amount = 20;
  print(f"${amount}");
else:
  amount = 100;
  print(f"${amount}");