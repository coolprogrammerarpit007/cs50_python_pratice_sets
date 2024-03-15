expression = input('Expression: ');
x,y,z = expression.split(' ');
x = int(x);
z = int(z);
result = 0.0;
if(y == '+'):
  result = x + z;
elif(y == '-'):
  result = x-z;
elif(y == '*'):
  result = x*z;
elif(y == '/'):
  result = x/z;
else:
  print('Inalid Operator');


print(round(float(result),1));