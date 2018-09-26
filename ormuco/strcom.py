''' Author May Zhang
    09/26/2018'''

'''
   String compare function
'''
def strcomp(strpair):
    strlist = strpair.split()
    x = strlist[0]
    y = strlist[1]

    if len(x) > 10 or len(y) > 10: # limit string length
        print("String length should be less than 10")
        return

    if x > y:
        print( x, "is grater than", y)
    elif x == y:
        print(x, "is equal to", y)
    else:
        print(x, "is less than", y)




'''
   testcase can be input from user or read from the file
'''
strin = input("please input two strings to compare: ")

if strin is not '':
    strcomp(strin)
else:
    with open('words.txt') as f:
        for line in f:
            strcomp(line)
