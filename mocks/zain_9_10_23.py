# // given a list of strings, return the string that is the longest common prefix of all strings in the list
from subprocess import list2cmdline


def find_longest(string_list):
    prefixes = {}
    return_string = ""
    # Loop over each string inside list
    for item in string_list:
        prefix = ''
        for char in item:
            prefix += char
            if prefix not in prefixes:
                prefixes[prefix] = len(prefix)
    # Loop over each prefix inside of dictionary
    max_length = 0

    for key, value in prefixes.items():
        present = True
        for item in string_list:
            if not item.startswith(key):
                present = False
        if present: 
            if value > max_length:
                return_string = key

    return return_string

list1 = ['tree', 'tried', 'triangle']
list2 = ['', 'tree', 'tried']

#print(f'The longest common prefix is: {find_longest(list2)} , finished')

 #list2 = []

# Looking at lines 8-15, we can say that when loop over n strings, 
# with each string having an average of m characters, O(n*m)     
# 
# Looking at lines 18-25, we can say that when we iterate over n*m prefixes in the hashmap,
# we then look at n strings from the inputed list, O(n*m * n)
# Time complexity: Since O(n^2*m) outclasses O(n*m), we can say that O(n^2*m) is our time complexity

# Space complexity: O(n*m^2)

# Instead of looping over every string in the input list, we loop over one string. We then
# check each prefix from the string, against other strings. 
# O(m), O(n*m)
# Space complexity: O(1)
# 
# 
def new_solution(string_list):
    prefix = string_list[0]
    if prefix == '':
        return ""
    for index in range(1, len(string_list)):
        while not string_list[index].startswith(prefix):
            prefix = prefix[0:-1]
    return prefix
        
list1 = ['tree', 'tried', 'triangle']
list2 = ['', 'tree', 'tried']

print(f'The longest common prefix is: {new_solution(list1)} , finished')

    

            

