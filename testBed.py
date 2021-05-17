import Payload
import time

import loopy1
import loopy2

### REF: https://stackabuse.com/search-algorithms-in-python/#fibonaccisearch

dic = Payload.RandomString()
search = '2LNT4bvRtUA7XtIgtAmz'



##################################
### loopy1 Search
start = time.time()
# # Algorithem starts here
x = loopy1.Search(dic , search)
print("Loopy1 Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("loopy1 Search Time:  " + str(end-start))
print()

##################################
### loopy2 Search

start = time.time()
# # Algorithem starts here
x = loopy2.Search(dic , search)
print("Loopy2 Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("loopy2 Search Time:  " + str(end-start))
print()