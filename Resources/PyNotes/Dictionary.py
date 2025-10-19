# dictionary = A changeable, unordererd collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washingon DC',
           'India':'New Delhi',
           'China':'Beijing',
           'Russia':'Moskow'}

capitals.update({'Germany':'Berlin'})
capitals.pop('China')
capitals.clear()

print(capitals['Germany'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)