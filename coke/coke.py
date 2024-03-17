# Amount of coke is 50 Cents.
# It accept amount only in these notations: 5,10,25 (in cents)

amount_due = 50;

while True:
  print(f"Amount Due: {amount_due}");
  amount = int(input('Insert Coin: '))
  if(amount == 5 or amount == 10 or amount == 25):
    amount_due = amount_due - amount
    print(f"Amount Due: {amount_due}");
    if(amount_due == 0 ):
      print(f"Change Owed: {amount_due}")
      break;
  continue

