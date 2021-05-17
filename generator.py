# from random_word import RandomWords
# r = RandomWords()

# x = r.get_random_words(maxDictionaryCount=400, hasDictionaryDef='true')

# print(x)

import random
import string

output_string = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(10))

print(output_string) 