data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']


for msg in data:
    print(msg)


print('-------------------------')

for msg in data:
    elements = msg.split(":")
    print(elements[0].upper(), elements[1])

print('-------------------------')

for msg in data:
    elements = msg.split(":")
    if elements[0] == "Error":
        print(elements[0].upper(), elements[1])
    else:
        print(elements[0], elements[1])
