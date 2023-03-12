# Напишите программу, которая принимает имя файла и выводит его расширение. 
# Если расширение у файла определить невозможно, выбросите исключение.

file_name = 'info.txt'
if '.' not in file_name or file_name[-1] == '.':
    raise ValueError('the file has no extension')
file_name = file_name.split('.')
print(f'Ext - {file_name[-1]}')