#Doing python coding for AdventOfcode. Belos is my 2nd day coding 1st code. 
#--- Day 2: Rock Paper Scissors --- , https://adventofcode.com/2022/day/2
#impyt downloaded from url : https://adventofcode.com/2022/day/2/input

#Creating a empyt list to store all input from file as list
data=[]

#Opening the file and replacing "\n" character while storing it in list

with open('Day2-adventOfCode1/input.txt') as f:
    for i in f.readlines():
        data.append(i.replace('\n',''))
    f.close()
#print(data)

# Creating a empty list to store score based on the my actions and calculating total score. 

my_Score=[]
for i in data:
    #print(i[0],i[2])
    if (i[0]=='C') and (i[2]=='Z'):
        #print(i[0],i[2],3)
        my_Score.append(3+3)
    elif (i[0]=='B') and (i[2]=='Y'):
        #print(i[0],i[2],3)
        my_Score.append(2+3)
    elif (i[0]=='A') and (i[2]=='X'):
        #print(i[0],i[2],3)
        my_Score.append(1+3)
    elif (i[0]=='C') and (i[2]=='Y'):
        #print(i[0],i[2],1)
        my_Score.append(2)
    elif (i[0]=='B') and (i[2]=='X'):
        #print(i[0],i[2],1)
        my_Score.append(1)
    elif (i[0]=='A') and (i[2]=='Z'):
        #print(i[0],i[2],1)
        my_Score.append(3)
    elif (i[0]=='C') and (i[2]=='X'):
        #print(i[0],i[2],1)
        my_Score.append(1+6)
    elif (i[0]=='B') and (i[2]=='Z'):
        #print(i[0],i[2],1)
        my_Score.append(3+6)
    elif (i[0]=='A') and (i[2]=='Y'):
        #print(i[0],i[2],1)
        my_Score.append(2+6)
    else:
        #print(i[0],i[2],8)
        my_Score.append(0)

#print(my_Score)

#Calculating total score
print("your total score be if everything goes \
exactly according to your strategy guide?  ", \
sum(my_Score))