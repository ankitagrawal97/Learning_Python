# THis is a string object #
name = 'Ankit'

if name.startswith('Ank'):
    print('Yes, the string starts with Ank')

if 'n' in name:
    print('Yes, the contains the string "n"')

if name.find('kit') != -1:
    print('Yes, it contains the string "kit"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))