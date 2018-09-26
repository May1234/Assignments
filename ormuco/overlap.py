''' Author May Zhang
    09/26/2018'''

import re

line1 = input("Please input the first two numbers:" )
line2 = input("Please input the second two numbers:" )

x = re.split(r',\s*|\s+', line1)
y = re.split(r',\s*|\s+', line2)

# If the second number in the first input is bigger
#the first number in the second input the lines will overlap
if x[1] > y[0]:

    print("Two lines overlap")
else:
    print("Two lines don't overlap")
