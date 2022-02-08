hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[0] = 'ENJOY THE SILENCE'

hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()

additionalSongs = ['NOTHING COMPARES 2 U',  'WISH YOU WERE HERE']

print(hitsToRead.pop(0))
print(hitsToRead.pop(0))

print(hitsTitles)
print(hitsToRead)
print(additionalSongs)

