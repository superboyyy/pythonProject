names = ['Andy', 'Becky', 'Candy', 'Duck', 'Elio']
for i in names:
    print(f'I invite {i} to my dinner.')

print(f'But {names[3]} cannot do that.')

names[3] = 'Debbie'
for i in names:
    print(f'I invite {i} to my dinner.')

print('I find a bigger table, so more friends will be invited.')

names.insert(0, 'Alice')
names.insert(3, 'Conda')
names.append('Florida')
for i in names:
    print(f'I invite {i} to my dinner.')

new = ''
while (len(names) >= 2):
    new = names.pop(0)
    print(f'{new} cannot come to my dinner.')

for i in names:
    print(f'{i} can still come to my dinner.')

while (len(names) != 0):
    del names[0]
print(names)

print(len(names))