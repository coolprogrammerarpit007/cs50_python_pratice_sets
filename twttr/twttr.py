tweet = input('Input: ');
short_tweet = '';

for letter in tweet:
  if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' ):
    continue
  else:
    short_tweet = short_tweet + letter;

print(f'Output: {short_tweet}');
  