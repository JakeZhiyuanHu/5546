i = 1
test = i == 1   # --> True
print(test)

lst1 = ['a']
print(f'This is lst1: {lst1}')

lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')

lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")

print(f"This is lst1 after modifying lst3: {lst1}")