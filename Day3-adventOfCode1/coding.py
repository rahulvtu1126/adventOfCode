#Doing python coding for AdventOfcode. Below is my 3rd day coding 1st code. 
#--- Day 3: Rucksack Reorganization --- , https://adventofcode.com/2022/day/3
#impyt downloaded from url : https://adventofcode.com/2022/day/3/input

#Creating a empyt list to store all input from file as list

data=[]

#Opening the file and replacing "\n" character while storing it in list

with open('Day3-adventOfCode1/input.txt') as f:
    for i in f.readlines():
        data.append(i.replace('\n',''))
    f.close()
print(len(data))

#fetching common letters from each compartments
priorities_data=[]
for i in data:
    #print(i[0:10])
    a=i[0 : int(len(i)/2)]
    b=i[int(len(i)/2) : ]
    #print(set(a).intersection(set(b)))
    for value in set(a).intersection(set(b)):
        priorities_data.append(value)

#fetching letters and assigning number to each number

dict_letter={}
import string
for i,j in enumerate(string.ascii_letters):
    dict_letter[j]=i+1

#fetching priorioty number for each line

priority_list=[]

for i in priorities_data:
    priority_list.append(dict_letter[i])

#fetching sum of priorioty number

print(sum(priority_list))

                

