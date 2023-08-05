#Doing python coding for AdventOfcode. Below is my 3rd day coding 2nd code. 
#--- Day 3: Rucksack Reorganization --- , https://adventofcode.com/2022/day/3
#impyt downloaded from url : https://adventofcode.com/2022/day/3/input

#Creating a empyt list to store all input from file as list

data=[]

#Opening the file and replacing "\n" character while storing it in list

with open('Day3-adventOfCode2/input.txt') as f:
    for i in f.readlines():
        data.append(i.replace('\n',''))
    f.close()
#print(len(data))

# Group 3 line in 1 list

itrte_data=[]
for i,j in enumerate(data):
    i=i+1
    #print(i,j)
    if i == 0:
        pass
    elif i%3==0:
        itrte_data.append(data[i-3:i])
#print((itrte_data))

#fetching common letter from one compartmnet which was fetched in last step
priorities_data=[]

for i in itrte_data:
    for a in (set(i[0]).intersection(set(i[1]))).intersection(set(i[2])):
        #print(a)
        priorities_data.append(a)

#fetching letters and assigning number to each number
dict_letter={}
import string
for i,j in enumerate(string.ascii_letters):
    dict_letter[j]=i+1

#fetching priorioty number for compartment

priority_list=[]
for i in priorities_data:
    priority_list.append(dict_letter[i])

#fetching sum of priorioty number
print(sum(priority_list))

                

