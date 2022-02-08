def PrintAnimal(*animals):
    #wyświetla określone w parametrze funkcji zwierze
    cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
    bear = r'''
    / \.-"""-./ \
    \   -   -   /
    |   o   o   |
    \  .-'"'-.  /
     '-\__Y__/-'
        `---`'''
    bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''

    for animal in animals:
        if animal == 'cat':
            print(cat)
        elif animal == 'bear':
            print(bear)
        elif animal == 'bat':
            print(bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return

# if PrintAnimal(''):
#     print('True')
# else:
#     print('False')
#
# if PrintAnimal('bat'):
#     print('True')
# else:
#     print('False')
#
# if PrintAnimal('cat'):
#     print('True')
# else:
#     print('False')
#
# if PrintAnimal('bear'):
#     print('True')
# else:
#     print('False')

PrintAnimal('cat', 'bat', 'bear')

#----------------------------------------------

from datetime import date

# def DaysToEndOfYear(year = date.today().year, month = date.today().month, day = date.today().day):
#     date_today = date(year, month, day)
#     #current_year = date_today.year
#     date_end_year = date(year, 12, 31)
#     delta = date_end_year - date_today
#     return delta.days


def DaysToEndOfYear(*dates):

    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date: ', date_today, 'dni do sylwestra:',  delta.days)
    return




#print(DaysToEndOfYear())
print(DaysToEndOfYear(date(2009,3,12), date(2011,4,29), date(2021,12,2)))