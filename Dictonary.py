chanels = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV Sport':700 }
print(chanels['Email'])
print(chanels)

chanelsUpdate = {'Natural Traffic':520, 'News':600}
chanels.update(chanelsUpdate)
print(chanels)

print(chanels.keys())

chanels.pop('Email')
print(chanels)
