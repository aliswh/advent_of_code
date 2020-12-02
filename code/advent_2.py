# https://adventofcode.com/2020/day/2

import time, re 

start = time.time_ns()

#input and clear file
input_file = open('inputs/input_2.txt')
input_array = [str(x) for x in input_file]
input_array = [x.replace('\n', '') for x in input_array]

howmany = 0

# part 1
var = re.compile(r'(?P<policy_s>\d+)-(?P<policy_e>\d+) (?P<letter>[a-z]): (?P<password>\w+)')
for i in input_array:
    occ = var.search(i)
    if occ:
        # get interval of accepted occurencies
        interv = list(range(int(occ.group('policy_s')), int(occ.group('policy_e'))+1))
        letter_occ = len(re.findall(occ.group('letter')+'{1}', occ.group('password')))
        if letter_occ in interv:
            howmany += 1


# part 2
howmany_part2 = 0
for i in input_array:
    occ = var.search(i)
    if occ:
        # get interval of accepted occurencies
        interv = [int(occ.group('policy_s')), int(occ.group('policy_e'))]
        try:
        # XOR : one position not both
            if (occ.group('password')[interv[0]-1] == occ.group('letter')) ^ (occ.group('password')[interv[1]-1] == occ.group('letter')):
                howmany_part2 += 1
        except IndexError: 
            continue
        


print(howmany, howmany_part2)

end = time.time_ns()
print((end-start)/10000)