# https://adventofcode.com/2020/day/1

# Find the 2 numbers that summed together equal 2020 and return their multiplication

import time 

start = time.time_ns()

input_file = open('input.txt')
input_array = [int(x) for x in input_file]

# sort by incremental order
input_array = sorted(input_array)
#print(input_array)

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
                print('Part 1 numbers:', input_array[len(input_array)-i], input_array[j], '=', r)
                return(input_array[len(input_array)-i] * input_array[j])
                
result_1 = get2020()
print('Part 1 result:', result_1)

# part 2: the same but with 3 numbers
# if the sum is less than 2020, look for the number equal to 2020 minus the sum in the array
# the search can be optimized but I'm tired :)

def get2020_part2():
    index = 0
    for i in range(1, len(input_array)):
        for j in range(index, len(input_array)):
            r = input_array[len(input_array)-i] + input_array[j]
            look_for_me = 2020 - r
            if r > 2020:
                break
            elif r < 2020:
                if look_for_me in input_array:
                    print('Part 2 numbers:', input_array[len(input_array)-i], input_array[j], look_for_me, "=", look_for_me+r)
                    return(input_array[len(input_array)-i] * input_array[j] * look_for_me)

result_2 = get2020_part2()
print('Part 2 result:', result_2)

end = time.time_ns()
print((end-start)/10000)
