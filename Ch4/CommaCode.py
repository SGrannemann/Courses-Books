def ListComma(list):
    myString = ''
    if not list:
        print("The list is empty!")
#    else:
#        for index in range(len(list)):
#            if index == len(list) - 1:
#                myString += ', and {}'.format(list[index])

#            elif index == 0:
#                myString += '{}'.format(list[index])
#            else:
#                myString += ', {}'.format(list[index])

    else:
        for index, string in enumerate(list):
            if index == len(list) - 1:
                myString += ', and {}.'.format(string)
            elif index == 0:
                myString += '{}'.format(string)
            else:
                myString += ', {}'.format(string)
        print(myString)

spam = ['apples', 'bananas', 'tofu', 'cats']
#spam = []
#spam = [1, 2, 3]
ListComma(spam)
