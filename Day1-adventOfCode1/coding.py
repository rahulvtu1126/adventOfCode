#Doing python coding for AdventOfcode. Below is my 1st day coding 1st code. 
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

#printing the max of list from elf_sum_list which consist of sum of each sub list.

print("Find the Elf carrying the most Calories. \
      How many total Calories is that Elf carrying?",\
        max(elf_sum_list))