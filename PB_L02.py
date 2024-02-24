import random
import string
import copy
from collections import defaultdict
#1. create a list of random number of dicts (from 2 to 10)

#creating list of dic's
dl = []
#generating list of random values of dics
for i in range(random.randint(2,10)):
    #define size of dic from 1 to 26
    s = random.randint(1,26)
    #define letters for key in dic
    k = random.sample(string.ascii_lowercase,s)
    #define random integer number from 1 to 100 for each key of dictionary
    v = (random.randint(1,100) for i in range(s))
    #zipping keys with values
    d = dict(zip(k,v))
    #adds dictionary to the end list
    dl.append(d)
#display generated list
print(dl)

#2. get previously generated list of dicts and create one common dict:
#if dicts have same key, we will take max value, and rename key with dict number with max value
#if key is only in one dict - take it as is
#creating copy for experiments
dl_c = copy.copy(dl)


#displaying copied list of dictionary
print(dl_c)


res_set = defaultdict(int)
for i in dl_c:
    for key, val in i.items():
      #res_set[f"{key}_{dl_c.index(i)}"] = max(res_set[key], val)
        res_set[key]  = max(res_set[key], val)

#sorting result set
sorted_dict = dict(sorted(res_set.items()))
# printing result
print("Max values dictionary: " )
print(sorted_dict)

