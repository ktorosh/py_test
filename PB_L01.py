import numpy as np
# creating array of 100 integers from 1 to 1000
randnums = np.random.randint(1, 1001, 100)
# displaying created array in the screen
print(randnums)

# defining function for ascending sorting
def asc_sort(arr):
# variable n is equal to lenght of array which should be sorted
    n = len(arr)
# creating loop for check each of element in array
    for i in range(n):
# element i is the last in the array
# for each element that possition is previous to i:
        for j in range(0, n - i - 1):
# checking if this element is higher that next then it is putting to the last possition
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# running asc_sort funtion on the created array
asc_sort(randnums)
# displaying sorted array
print("ASC sorted array:", randnums)

#def desc_sort(arr):
#    n = len(arr)
#    for i in range(n):
#        for j in range(0, n - i - 1):
#            if arr[j] < arr[j + 1]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#desc_sort(randnums)
#print("DESC sorted array:", randnums)

#define fuction for calucalating avarage
def even_avg(even_arg):
    return sum(even_arg) / len(even_arg)

#create array even_arg of even numbers from randnums
even_arg = randnums[randnums%2==0]

#running function even_avg
even_average = even_avg(even_arg)
print('Average of even numbers from arrayis:',even_average)

#define fuction for calucalating avarage
def odd_avg(odd_arg):
    return sum(odd_arg) / len(odd_arg)

#create array odd_arg of even numbers from randnums
odd_arg = randnums[randnums%2!=0]

#running function odd_avg
odd_average = odd_avg(odd_arg)
print('Average of odd numbers from arrayis:',odd_average)
