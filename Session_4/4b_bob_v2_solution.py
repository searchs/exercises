to_bob = input('What would you like to say to Bob?\n')

greetings = ['hi', 'hey', 'hello', 'howdy']

if to_bob.lower() in greetings:
    print('...sup')
# Below from Session 2
elif '?' in to_bob and '!' in to_bob:
    print('Calm down, I know what I\'m doing!')
elif '?' in to_bob:
    print('Sure.')
elif '!' in to_bob:
    print('Whoa, chill out!')
elif to_bob == '':
    print('Fine. Be that way!')
else:
    print('Whatever.')
