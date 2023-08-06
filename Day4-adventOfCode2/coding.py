#Getting input data from file
data=[]
with open('Day4-adventOfCode2/input.txt') as f:
    for i in f.readlines():
        data.append(i.replace('\n',''))

#getting subset value in list 
subset_value=[]
for i in data:
    #print(i.split(',')[0],' , ',i.split(',')[1])
    #spliting lines based on comma delimited
    a1=i.split(',')[0].split('-')[0]
    a2=i.split(',')[0].split('-')[1]
    b1=i.split(',')[1].split('-')[0]
    b2=i.split(',')[1].split('-')[1]
    #print(a1)
    #putting a1,a2 and b1,b2 range values in seperate list to compare.
    compare_list1=[]
    compare_list2=[]
    for i in range(int(a1),int(a2)+1):
        compare_list1.append(i)
    for i in range(int(b1),int(b2)+1):
        compare_list2.append(i)
    
    #check whether any of the element from each set is part other set

    if set(compare_list1).intersection(compare_list2):
        subset_value.append(1)
    else:
        subset_value.append(0)

# print subset and sum of the subset
#print(subset_value)
print(sum(subset_value))