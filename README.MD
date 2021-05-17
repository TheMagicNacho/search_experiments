# Notes on Search Research and implimentation with API Objects

### 20210509
All search algorithems fail at an index of 3,000. I believe this has to do with memory. I can't imagine needing an index this large though.

Using the loopy algorithems, validating the input with an if statement  makes the algorithem slower by 0.00001 seconds.
However, if there is an error validating the input will allow the system to increase speed by 3 x10^5 seconds.

*Times with no error*
**validating**
Loopy1 Search Result:  [182]
loopy1 Search Time:  0.00014543533325195312
**non-validating**
Loopy2 Search Result:  [182]
loopy2 Search Time:  0.00013685226440429688

*Times with an input error*
**validating**
Loopy1 Search Result:  -1
loopy1 Search Time:  3.814697265625e-05
**non-validating**

Loopy2 Search Result:  []
loopy2 Search Time:  0.00010371208190917969

### 20210511
When trying to apply the integer search algorethems with an object the entire program fails.
Is it possible to encode objects in to a binary then search as an integer?

### 0210515
Okay. Turns out, that we don't need the loopy algoritem because I just need to know if the item exists in the dictionary object.
Then it returns the object.


Where I left off:
I have the search algoitem working properly now.
It will add the chosen object.

Now I need to attach it this to resolve.

### 20210516
Implemented the search algo with Resolve. Increased performance.
```
Original performance time:  2.314 s
Improved performance time:  2.055 s
```

# RFI
> Is there a novel way to encode an object into a integer for easy manipulation?