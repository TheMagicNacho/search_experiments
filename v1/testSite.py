import time
import Payload
import Binary
import Jump
import Fibonacci
import Interpolation
import Exponential
import Linear
import loopy


### REF: https://stackabuse.com/search-algorithms-in-python/#fibonaccisearch

dic = Payload.RandomString()
search = 'KEQw6KGtxx685L09W4lo'



##################################
### Binary Search

start = time.time()
# # Algorithem starts here
x = Binary.Search(dic , search)
print("Binary Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("Binary Search Time:  " + str(end-start))
print()

##################################
### Jump Search
start = time.time()
# # Algorithem starts here
x = Jump.Search(dic , search)
print("Jump Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("Jump Search Time:  " + str(end-start))
print()


##################################
### Fibonacci Search
start = time.time()
# # Algorithem starts here
x = Fibonacci.Search(dic , search)
print("Fibonacci Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("Fibonacci Search Time:  " + str(end-start) )
print()

##################################
### Exponential Search
start = time.time()
# # Algorithem starts here
x = Exponential.Search(dic , search)
print("Exponential Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("Exponential Search Time:  " + str(end-start))
print()

##################################
# NOTE: Only works with int, and not sting.

# ### Interpolation Search
# start = time.time()
# # # Algorithem starts here
# x = Interpolation.Search(dic , search)
# print("Interpolation Search Result:  " + str(x))
# # # Algoritem stops here
# end = time.time()
# print("Interpolation Search Time:  " + str(end-start))
# print()


# ##################################
# ### Linear Search
# start = time.time()
# # # Algorithem starts here
# x = Linear.Search(dic , search)
# print("Linear Search Result:  " + str(x))
# # # Algoritem stops here
# end = time.time()
# print("Linear Search Time:  " + str(end-start))
# print()

##################################
### KMP (string) Search
start = time.time()
# # Algorithem starts here
x = loopy.Search(dic , search)
print("kmp Search Result:  " + str(x))
# # Algoritem stops here
end = time.time()
print("kmp Search Time:  " + str(end-start))
print()
