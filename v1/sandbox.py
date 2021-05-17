import math
import random
import string

totalRange= 1000

# ### Ordered Integer generator
# intList = []
# for i in range(totalRange):
#     intList.append(i+1)
# print(intList)


## String Generator
strList = []
for i in range(totalRange):
    strList.append(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20)))
print(strList)


# ### Random Integer Generator
# randList = []
# for i in range(totalRange):
#     randList.append(random.randint(100,1000))
# print(randList)