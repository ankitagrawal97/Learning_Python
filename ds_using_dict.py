ab = {
    'Ankit': 'ankit.k.agrawal97@gmail.com',
    'Ankit Agrawal': '171210010@nitdelhi.ac.in',
    'Matsumoto': 'matz@ruby-lang.org'
}

print('Ankit Address is', ab['Ankit'])

# Deleting a key-value pair
del ab['Matsumoto']

print('\nThere are {} contact in the address book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} is at {}' .format(name, address))

# Adding a key-value pair
ab['shamyak'] = 'shamyakioi.gmo'

print('Address of Shamyak is ',ab['shamyak'])

ab.a