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

# Initialize a dictionary to store the maximum values and their corresponding index
res_set = defaultdict(lambda: {'max_val': 0, 'index': None})

# Iterate through the dictionaries in dl_c
for idx, i in enumerate(dl_c):
    for key, val in i.items():
        # If the current value is greater than the stored maximum value, update the dictionary
        if val > res_set[key]['max_val']:
            res_set[key]['max_val'] = val
            res_set[key]['index'] = idx

# Convert the defaultdict to a regular dictionary
sorted_dict = {f"{key}_{res_set[key]['index']}": val['max_val'] for key, val in res_set.items()}

# Sort the sorted_dict in ascending order by key
sorted_dict = dict(sorted(sorted_dict.items(), key=lambda item: item[0]))

# Print the maximum values dictionary
print("Max values dictionary:")
print(sorted_dict)