
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
capCapital = 0
year = 1
capCapital = initialCapital


while year <= maxTimeYears:
    newCapital = round(capCapital + (capCapital * percent), 2)
    print('Year ', year, 'capital: ', newCapital)
    capCapital = newCapital
    year += 1
else:
    print('Total profit', capCapital - initialCapital)


print('--------------------------------------------------------')



number=20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)
print('-------------------------------------------------------')



tekst = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

wordLength = 6
listOfWords = tekst.split(' ')
sumWords = 0
shortWords = 0
longWords = 0
i = 0
print(listOfWords)

for word in listOfWords:
    if len(word) > wordLength:
        sumWords +=1


print('ilość słów dłuższych od ', wordLength, 'wynosi', sumWords)



while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1
    i += 1

print('w tekscie jest', longWords, 'długich słów i', shortWords, 'krótkich')
    

