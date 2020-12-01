# https://adventofcode.com/2020/day/1

import time 

start = time.time_ns()

input_file = open('input.txt')
input_array = [int(x) for x in input_file]

# sort by incremental order
input_array = sorted(input_array)
print(input_array)

# Sum values starting from the last. Add the first. If the results is bigger than 2020, shift from the largest value to the second largest.
# If the sum is less than 2020, shift from the first value to the second. 
# Break the cycle when you reach 2020.
def get2020():
    index = 0
    for i in range(1, len(input_array)):
        for j in range(index, len(input_array)):
            r = input_array[len(input_array)-i] + input_array[j]
            if r > 2020:
                break
            elif r < 2020:
                index += 1 
            else:
                return(input_array[len(input_array)-i] * input_array[j])
                
risultato = get2020()
print(risultato)

end = time.time_ns()
print((end-start)/10000)