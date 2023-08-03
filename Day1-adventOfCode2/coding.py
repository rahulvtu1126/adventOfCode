#Doing python coding for AdventOfcode. Belos is my 1st day coding 2nd code. 
#--- Day 1: Calorie Counting --- , https://adventofcode.com/2022/day/1
#impyt downloaded from url : https://adventofcode.com/2022/day/1/input

#Creating a empty list

list1=[]

#opening input file which was downloaded from https://adventofcode.com/2022/day/1/input

with open("/home/om/Documents/adventOfCode/Day1-adventOfCode2/input.txt",'r') as a:
    for i in a.readlines():
        list1.append(i.replace('\n',''))

# coverting string element to integer

for i in range(0,len(list1)):
    if list1[i]:
        list1[i]=int(list1[i])
    else:
        list[i]
#print(list1)

#Creating sub list by grouping the elemnts based on empty element in between the list

from itertools import groupby
elf_lists=[list(g) for k, g in groupby(list1, key=bool) if k]
#print(final_list)

# finding the sum of each sub list. 

elf_sum_list=[]
for i in elf_lists:
    elf_sum_list.append(sum(i))

#printing the sum of top 3 list sum

print("Find the top three Elves carrying the most Calories. \
      How many Calories are those Elves carrying in total? ", \
        sum(sorted(elf_sum_list, reverse=True)[0:3]))