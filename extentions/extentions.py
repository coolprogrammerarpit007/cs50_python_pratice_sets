file = input('File name: ');
if('.' in file):
  extention = file.split('.')[1].lower();
  file_type = '';
else:
  extention = '';

match extention:
  case 'gif':
    file_type = f"image/{extention}";
  case 'jpg'|'jpeg':
    file_type = 'image/jpeg';
  case 'png':
    file_type = f"image/{extention}";
  case 'pdf':
    file_type = f"application/{extention}";
  case 'txt':
    file_type = f"application/{extention}";
  case 'zip':
    file_type = f"application/{extention}";
  case _:
    file_type = f"application/octal-stream"

print(file_type);




