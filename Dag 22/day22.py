from aoc import read_input

# input
secret_numbers = map(int,read_input("inputdag22"))
#secret_numbers = [1,2,3,2024]

# part 1
def secret_number(number):
    result = number*64
    number ^= result
    number %= 16777216
    result = number//32
    number ^= result
    number %= 16777216
    result = number*2048
    number ^= result
    number %= 16777216
    return number
    
total = 0
dict_all = {}
for number in secret_numbers:
    start_number = number
    dict_number = {}
    start = (0,0,0,0)
    digit = int(str(number)[-1])
    index = 0
    for i in range(2000):
        number = secret_number(number)
        new_digit = int(str(number)[-1])
        diff = new_digit - digit
        digit = new_digit
        start = start[1:4] + (diff,)
        if start not in dict_number and i >=3:
            dict_number[start] = new_digit
    dict_all[start_number] = dict_number
    total += number
print(total)
    
# part 2
all_diffs = set()
for key,dict_number in dict_all.items():
    for diff,value in dict_number.items():
        all_diffs.add(diff)
        
max_bananas = 0
for diff in all_diffs:
    bananas = 0
    for number,dict_number in dict_all.items():
        bananas += dict_number.get(diff,0)
    max_bananas = max(max_bananas,bananas)
print(max_bananas)     
        
        
        
        
        
        
        
        
        