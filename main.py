# How many vowels in a string

from collections import Counter


sentence = 'mississw5yesdhfgsdrfgsegippi'
c = Counter(sentence.lower())
print(c)

counter = sum(c[v] for v in set('aeiou'))

print(counter)



